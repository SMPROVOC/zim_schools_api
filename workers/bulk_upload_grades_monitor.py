import json
import time
from datetime import datetime, timedelta
from dotenv import load_dotenv
from sqlalchemy import or_, and_
import pandas as pd
from utils import database as db
from utils import models, schema
from utils.functions import generator_id

load_dotenv(override=True)

print('Worker has started....')
def grademe(student_mark, marking_schema):
    # default_scheme = {'E': 30, 'D': 50, 'C': 60, 'B': 70, 'A': 100}

    scheme = {'E': 30, 'D': 50, 'C': 60, 'B': 70, 'A': 100}

    if marking_schema:
        scheme = json.loads(marking_schema.Structure)

    if 0 < student_mark <= scheme['E']:
        return {'grade': 'E', 'mark': student_mark}

    if scheme['E'] < student_mark < scheme['D']:
        return {'grade': 'D', 'mark': student_mark}

    if scheme['D'] <= student_mark < scheme['C']:
        return {'grade': 'C', 'mark': student_mark}

    if scheme['C'] <= student_mark < scheme['B']:
        return {'grade': 'B', 'mark': student_mark}

    if scheme['B'] <= student_mark <= scheme['A']:
        return {'grade': 'A', 'mark': student_mark}

while True:

    jobs = db.session.query(models.GradeWorker).filter(models.GradeWorker.Status == 'pending').all()

    skipped_student_names = []

    if jobs:
        for job in jobs:

            try:
                # print(job.File_path)
                df = pd.read_csv(job.File_path)

                if 'Level' not in df.columns or 'Term' not in df.columns:
                    raise Exception('Missing column')

                for index, row in df.iterrows():
                    name_list = row["Student"].split(' ')
                    student_name = name_list[0]
                    student_surname = name_list[1]

                    # subject_id = db.session.query(models.Subjects).filter(models.Subjects.SUBID == request.HRID).first()
                    student = db.session.query(models.Student).filter(
                        and_(
                            models.Student.First_Name == student_name,
                            models.Student.Last_Name == student_surname
                        )).first()

                    if not student:
                        current_date_time = datetime.now()
                        exception_created_at = current_date_time.strftime('%Y-%m-%d %H:%M:%S')
                        skipped_student_names.append(f'{row["Student"]} -> Student record not found]')

                        print(f'[{exception_created_at}] [Record exception] [Student record not found] : {row["Student"]}')


                    if student:
                        student_id = student.SID

                        subject_list = []

                        # iterating the columns
                        for column_name in df.columns:
                            # print(type(column_name))
                            if column_name != 'Student' and column_name != 'Board' and column_name != 'Term' and column_name != 'Term':
                                subject_list.append(column_name)

                        marks_by_subject = {}
                        overall_grade_marks = 0
                        total_grade_loops = 0

                        marking_structure = db.session.query(models.GradingStructure).filter(
                            models.GradingStructure.Name == row["Board"]).first()

                        for subject in subject_list:
                            subject_qry = db.session.query(models.Subjects).filter(
                                models.Subjects.Name == subject
                            ).first()

                            if subject_qry:
                                grade_dict = grademe(row[subject], marking_structure)
                                overall_grade_marks = overall_grade_marks + grade_dict['mark']
                                total_grade_loops += 100
                                marks_by_subject[subject_qry.SUBID] = grade_dict

                        if not marking_structure:
                            print('no marking structure found for student')
                        student_school_id = db.session.query(models.StudentEnrollment).filter(
                            models.StudentEnrollment.SID == student.SID).first()

                        if not student_school_id:
                            print('student not found in student enrollment')

                        overall_grade_percentage = (overall_grade_marks / total_grade_loops) * 100
                        # print(overall_grade_marks)
                        # print(total_grade_loops)
                        # print(overall_grade_percentage)
                        # print(job.Uploaded_by)
                        # print(student.SID)
                        # print(student_school_id.SCID)
                        # print('Term', row["Term"])
                        # print(marking_structure.GSID)
                        school_term = f'Term {row["Term"]}'

                        check_grades = db.session.query(models.Grades).filter(and_(
                            models.Grades.SID == student.SID,
                            models.Grades.SCID == student_school_id.SCID,
                            models.Grades.Term == school_term
                        )).first()

                        # get  the current datetime
                        current_date_time = datetime.now()

                        # convert datetime to string format %Y/%m/%d %H:%M:%S
                        grades_created_at = current_date_time.strftime('%Y-%m-%d %H:%M:%S')

                        if not check_grades:
                            # create a new grade record

                            grade_id = generator_id('GID')
                            # create new grade in db
                            new_grade = models.Grades(

                                GID=grade_id,
                                UID=job.Uploaded_by,
                                SID=student.SID,
                                SCID=student_school_id.SCID,
                                Marks_By_Subject=json.dumps(marks_by_subject),
                                Term=school_term,
                                Level="O level (default)",
                                Percentage=overall_grade_percentage,
                                Grading_structure=marking_structure.GSID,
                                Created_at=grades_created_at,
                                Updated_at='Null',
                                Deleted_at='Null',
                            )

                            # add new student in db
                            db.session.add(new_grade)

                            db.session.commit()

                            print(f'[{grades_created_at}] [Created record] [processed] : {row["Student"]}')

                        if check_grades:
                            # update grade record
                            # create new student in db
                            check_grades.UID = job.Uploaded_by
                            check_grades.SID = student.SID
                            check_grades.SCID = student_school_id.SCID
                            check_grades.Marks_By_Subject = json.dumps(marks_by_subject)
                            check_grades.Term = school_term
                            check_grades.Level = "O level (default)"
                            check_grades.Percentage = overall_grade_percentage
                            check_grades.Grading_structure = marking_structure.GSID
                            check_grades.Updated_at = grades_created_at

                            # update new grades in db
                            db.session.commit()

                            print(f'[{grades_created_at}] [Updated record] [processed] : {row["Student"]}')


                job.Status = 'processed'
                job.Info = json.dumps(skipped_student_names)
                db.session.commit()

            except Exception as e:
                print(e)

    time.sleep(5)