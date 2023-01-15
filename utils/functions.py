import json
import os
import re
from datetime import datetime, timedelta
import random
from dotenv import load_dotenv
from passlib.context import CryptContext
from jose.exceptions import JWTClaimsError
from jose import JWTError, jwt, ExpiredSignatureError
from fastapi import HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import or_, and_
import pandas as pd

from utils import database as db
from utils import models, schema

load_dotenv(override=True)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def student_login(student_id, password):
    # Get email provided by the user from db
    student = db.session.query(models.Student).filter(models.Student.SID == student_id,
                                                      models.Student.Deleted_at == 'Null').first()

    # Check if the user details exists
    if not student:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    # Verify if password matches
    pwd_match = pwd_context.verify(password, student.Password)

    # Check if the password match
    if not pwd_match:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    # Create an access token
    access_token = create_access_token(data={'sub': student_id})

    # Create response dictionary/json
    response_dict = {
        'SID': student.SID,
        'Fullname': f'{student.First_Name} {student.Last_Name}',
        'Gender': student.Gender,
        'Hold_response': student.Hold_response,
        'Token': f'{access_token}',
    }

    return json.dumps(response_dict)


def student_get_info(student_id):
    # get student infomation
    student = db.session.query(models.Student).filter(models.Student.SID == student_id,
                                                      models.Student.Deleted_at == 'Null').first()

    if not student:
        raise HTTPException(status_code=400, detail="Student not found")

    # get student grades
    student_grades = db.session.query(models.Grades).filter(models.Grades.SID == student_id,
                                                            models.Grades.Deleted_at == 'Null').all()

    grades_list = {}

    if not student_grades:
        raise HTTPException(status_code=400, detail="Student grades record not found")

    for grade in student_grades:
        grades_list[grade.GID] = {'grading': json.loads(grade.Marks_By_Subject), 'school_id': grade.SCID,
                                  'Level': grade.Level, 'term': grade.Term,
                                  'grading_structure': grade.Grading_structure, 'percentage': grade.Percentage,
                                  'date_captured': grade.Created_at}

    # get student enrolled schools

    student_enrollments = db.session.query(models.StudentEnrollment).filter(models.StudentEnrollment.SID == student_id,
                                                                            models.StudentEnrollment.Deleted_at == 'Null').all()

    enrollment_list = {}

    if not student_enrollments:
        raise HTTPException(status_code=400, detail="Student enrollment record not found")

    for enrollment in student_enrollments:
        # current_enrollment_record = [enrollment.SCID, enrollment.Created_at]
        # enrollment_list.append(current_enrollment_record)
        enrollment_list[enrollment.EID] = {
            'school_id': enrollment.SCID, 'date_enrolled': enrollment.Created_at
        }

    # Create user dictionary
    student_dict = {
        'Name': student.First_Name,
        'Surname': student.Last_Name,
        'Gender': student.Gender,
        'DOB': student.DOB,
        'Address': student.Address,
        'Phone_number': student.Student_Cell_Number,
        'Guardian': student.Guardian_Full_Name,
        'Guardian_phone_number': student.Guardian_Cell_Number,
        'Grades': grades_list,
        'Enrolled_schools': enrollment_list

    }

    return json.dumps(student_dict)


def user_login(user_id, password):
    # Get email provided by the user from db
    user = db.session.query(models.Users).filter(models.Users.UID == user_id,
                                                 models.Users.Deleted_at == 'Null').first()

    # Check if the user details exists
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    # Verify if password matches
    pwd_match = pwd_context.verify(password, user.Password)

    # Check if the password match
    if not pwd_match:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    # Create an access token
    access_token = create_access_token(data={'sub': user_id})

    # Create response dictionary/json
    response_dict = {
        'UID': user.UID,
        'Fullname': f'{user.First_Name} {user.Last_Name}',
        'Gender': user.Gender,
        'Token': f'{access_token}',
    }

    return json.dumps(response_dict)


def search_student(search):
    search_results = db.session.query(models.Student).filter(
        or_(
            models.Student.SID.like(f'%{search}%'),
            models.Student.First_Name.like(f'%{search}%'),
            models.Student.Last_Name.like(f'%{search}%'),
            models.Student.Gender.like(f'%{search}%'),
            models.Student.Guardian_Full_Name.like(f'%{search}%'),
            models.Student.Guardian_Cell_Number.like(f'%{search}%'),
            models.Student.Student_Cell_Number.like(f'%{search}%'),
            models.Student.Address.like(f'%{search}%')
        )).limit(25).all()

    if not search_results:
        raise HTTPException(status_code=400, detail="No record found for you search.")

    return search_results


def create_access_token(data: dict):
    """
    Creates an access token for users to access routes
    :param data: is a string that can be encoded into the token and retrieved after its verified
    :return: jwt token
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=int(os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')))
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv('SECRET_KEY'), algorithm=os.getenv('ALGORITHM'))
    return encoded_jwt


def verify_token(token: str, access_rights: dict):
    try:
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='could not validate credentials',
            headers={'WWW-Authenticate': 'Bearer'},
        )

        payload = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=[os.getenv('ALGORITHM')])
        verified_token: str = payload.get("sub")
        if verified_token is None:
            raise credentials_exception
        token_data = schema.TokenData(token_otp=verified_token)
        verify_access(token_data.token_otp, access_rights)
        return token_data.token_otp

    except ExpiredSignatureError:
        raise HTTPException(status_code=403, detail="Token signature has expired ")
    except JWTClaimsError as error:
        raise HTTPException(status_code=403, detail=f"Incorrect : {error}")
    except JWTError:
        raise HTTPException(status_code=403, detail="Invalid token signature")


def verify_access(verified_user_id, path_access_rights: dict):
    """
    Function that verifies an access tokens validity
    :param verified_user_id: student id e.g SID00001
    :param path_access_rights: is a list of path access rights e.g ['sw', 'tr']
    :return: Exceptions
    """
    access_codes = db.session.query(models.PrivilegeHandler).filter(
        models.PrivilegeHandler.UID == verified_user_id).first()
    if not access_codes:
        raise HTTPException(status_code=403, detail='User privileges not found')

    user_privileges = json.loads(access_codes.Privilege)

    if not compare_access_data(user_privileges, path_access_rights):
        raise HTTPException(
            status_code=403, detail=f'Privilege restriction: required privileges {path_access_rights}')


def compare_access_data(privileges, rights):
    """
    Compares to find required privileges on 1 list against the other.
    :param list1: is a list of user access rights e.g ['sr', 'sd']
    :param list2: is a list of path access rights e.g ['sw', 'tr']
    :return: bool as true or false
    """
    result = False
    # parsed_privileges = json.loads(privileges)
    # print(privileges['permissions'])

    if privileges['hold_response'] != "HRID00":
        raise HTTPException(
            status_code=403, detail=f'Access denied with hold response {privileges["hold_response"]}')

    # traverse in the 1st list
    for user_rights in privileges['permissions']:

        # traverse in the 2nd list
        for path_rights in rights['required_permissions']:

            # if one common
            if user_rights == path_rights:
                # result = True
                # return result
                # traverse in the 1st list
                for user_role in privileges['roles']:

                    # traverse in the 2nd list
                    for path_roles in rights['required_roles']:

                        # if one common
                        if user_role == path_roles:
                            result = True
                            return result

    return result


def verify_headers(request):
    if request.headers.get('token') is None:
        raise HTTPException(
            status_code=403,
            detail=f'Access denied with no token header. Please include a token header with the token to pass validation.')

    return request.headers.get('token')


def generator_id(id_type):
    # global check
    global new_id
    check = True
    loop_count = 0

    while check:
        new_id = f'{id_type}{random.randint(1000, 9999)}'
        if id_type == 'UID':
            verify_id = db.session.query(models.Users).filter(models.Users.UID == new_id).first()
        elif id_type == 'SID':
            verify_id = db.session.query(models.Student).filter(models.Student.SID == new_id).first()

        elif id_type == 'PHID':
            verify_id = db.session.query(models.PrivilegeHandler).filter(models.PrivilegeHandler.PHID == new_id).first()

        elif id_type == 'HRHID':
            verify_id = db.session.query(models.HoldResponseHandler).filter(
                models.HoldResponseHandler.HRHID == new_id).first()

        elif id_type == 'SEID':
            verify_id = db.session.query(models.StudentEnrollment).filter(
                models.StudentEnrollment.SEID == new_id).first()


        elif id_type == 'GID':
            verify_id = db.session.query(models.Grades).filter(
                models.Grades.GID == new_id).first()

        elif id_type == 'UEID':
            verify_id = db.session.query(models.UserEnrollment).filter(
                models.UserEnrollment.UEID == new_id).first()

        else:
            return 'GIDERR00'  # id type not recognised. Try UID or SID

        if not verify_id:
            check = False

        if loop_count > 8999:
            check = False
            return 'GIDERR01'  # can not create id between range 1000 to 9999. They are all taken.

        loop_count += 1
        #print(loop_count)

    return new_id


def create_student_profile(request, user_id) -> dict:
    student_check = db.session.query(models.Student).filter(
        and_(
            models.Student.First_Name == request.First_Name,
            models.Student.Last_Name == request.Last_Name
        )).first()

    if student_check:
        print(student_check)
        raise HTTPException(status_code=403, detail=f'Student already exists')

        # generate a random student id for new student
    generated_student_id = generator_id('SID')

    # handle errors from generating student id
    if generated_student_id != 'GIDERR00' or generated_student_id != 'GIDERR01':

        first_name = request.First_Name.capitalize()
        last_name = request.Last_Name.capitalize()
        gender = request.Gender.capitalize()
        dob = request.DOB
        address = request.Address.capitalize()
        student_cell_number = request.Student_Cell_Number.capitalize()
        guardian_full_name = request.Guardian_Full_Name.capitalize()
        guardian_cell_number = request.Guardian_Cell_Number.capitalize()

        # validate DOB date format
        try:
            bool(datetime.strptime(request.DOB, '%Y-%m-%d'))
        except ValueError:
            raise HTTPException(status_code=403, detail=f'DOB format not correct. Try Y-m-d')

        # check if the first name contains any numbers
        if has_numbers(first_name):
            raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                                detail="first name can not contains numbers")

        # check if the last name contains any numbers
        if has_numbers(last_name):
            raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                                detail="last name can not contains numbers")

        # check if the guardian_full_name contains any numbers
        if has_numbers(guardian_full_name):
            raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                                detail="guardian full name can not contains numbers")

        # check if the gender contains any numbers
        if has_numbers(gender):
            raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                                detail="gender can not contains numbers")

        # validate gender to come as a single letter
        if len(gender) > 1:
            raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                                detail="gender can either be M or F")

        # check if the DOB contains any letters
        if not re.search(r"[A-Z a-z]", dob) is None:
            raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                                detail="DOB can not contains letters")

        # check if the student_cell_number contains any letters or special characters
        if not re.search(r"[ !@#$%&'()*+,-./[\\\]^_`{|}~A-Za-z" + r'"]', student_cell_number) is None:
            raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                                detail="student cell number can not contains other character")

        # check if the all cell number have 12 digits
        if len(student_cell_number) != 12 or len(guardian_cell_number) != 12:
            raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                                detail="all cell numbers must be 12 characters starting with 263")

        # check if the guardian_cell_number contains any letters or special characters
        if not re.search(r"[ !@#$%&'()*+,-./[\\\]^_`{|}~A-Za-z" + r'"]', guardian_cell_number) is None:
            raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                                detail="guardian cell number can not contains other characters")

        # check if the student_cell_number begin with 263
        if guardian_cell_number[:3] != '263' or student_cell_number[:3] != '263':
            raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                                detail="all cell numbers must begin with 263")

    # get  the current datetime
    current_date_time = datetime.now()

    # convert datetime to string format %Y/%m/%d %H:%M:%S
    student_created_at = current_date_time.strftime('%Y-%m-%d %H:%M:%S')

    # create new student in db
    new_student = models.Student(
        SID=generated_student_id,
        First_Name=first_name,
        Last_Name=last_name,
        Gender=gender,
        DOB=dob,
        Address=address,
        Guardian_Full_Name=guardian_full_name,
        Guardian_Cell_Number=guardian_cell_number,
        Student_Cell_Number=student_cell_number,
        Created_at=student_created_at,
        Updated_at='Null',
        Deleted_at='Null',
        Password='Default',
        Hold_response='Null'
    )

    # add new student in db
    db.session.add(new_student)

    # commit new student (True = error, False = success)
    if db.session.commit():
        raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                            detail="there was an error creating the student record")

    # generate a new privilege id for the student
    privilege_id = generator_id('PHID')

    # create new privilege in db
    new_student_privilege = models.PrivilegeHandler(
        PHID=privilege_id,
        Privilege=json.dumps({"roles": ["RID00004"], "permissions": ["PID00002"], "hold_response": "HRID00"}),
        UID=generated_student_id,
        Created_at=student_created_at,
        Updated_at='Null',
        Deleted_at='Null'
    )

    # add new privilege in db
    db.session.add(new_student_privilege)

    # commit new privilege
    if db.session.commit():
        raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                            detail="there was an error creating the student privileges")

    # generate a new hold response id for the student
    hold_response_id = generator_id('HRHID')

    # create new hold response in db
    new_student_hold_response = models.HoldResponseHandler(
        HRHID=hold_response_id,
        HR_CODE=json.dumps(['00']),
        UID=generated_student_id,
        Created_at=student_created_at,
        Updated_at='Null',
        Deleted_at='Null'
    )
    # add new hold responses in db
    db.session.add(new_student_hold_response)

    # commit new hold response
    if db.session.commit():
        raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                            detail="there was an error creating the student hold response")

    scid = ''

    school_enrolled_id = db.session.query(models.School).filter(models.School.SCID == request.School_enrolled).first()

    if not school_enrolled_id:
        scid = 'Default'
    else:
        scid = school_enrolled_id.SCID

    # generate a new enrollment id for the student
    enrollment_id = generator_id('SEID')

    # create enrollment in db
    new_enrollment = models.StudentEnrollment(
        SEID=enrollment_id,
        SID=generated_student_id,
        SCID=scid,
        Enrolled_By=user_id,
        Created_at=student_created_at,
        Updated_at='Null',
        Deleted_at='Null'
    )

    # add new enrollment in db
    db.session.add(new_enrollment)

    # commit new enrollment
    if db.session.commit():
        raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                            detail="there was an error creating the student erollment record")

    return {
        'message': 'student record created successfully',
    }


def update_hold_response(request, user_id) -> dict:
    check_id = db.session.query(models.HoldResponses).filter(models.HoldResponses.HRID == request.HRID).first()

    if not check_id:
        raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                            detail="invalid hold response id provided")

    user = db.session.query(models.HoldResponseHandler).filter(models.HoldResponseHandler.UID == request.SID).first()

    if not user:
        raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                            detail="student does not have a hold  response record")


    if request.HRID == user.HR_CODE:
        raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                            detail=f"hold response was already set for student {request.SID}")

    # get  the current datetime
    current_date_time = datetime.now()

    # convert datetime to string format %Y/%m/%d %H:%M:%S
    hr_updated_at = current_date_time.strftime('%Y-%m-%d %H:%M:%S')

    user.HR_CODE = request.HRID
    user.Updated_at = hr_updated_at
    db.session.commit()

    return {
        'message': f'student {request.SID} hold response updated successfully.'
    }


def update_student_privileges(request, user_id) -> dict:

    student = db.session.query(models.PrivilegeHandler).filter(models.PrivilegeHandler.UID == request.SID).first()

    if not student:
        raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                            detail=f"can not find student {request.SID} privileges")


    if 'roles' not in request.Privileges.keys():
        raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                            detail="the privileges provided have a wrong format, privileges must be the format {'roles': ['role_id'], 'permissions':['permission_id']} as a dictionary")


    if 'permissions' not in request.Privileges.keys():
        raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                            detail="the privileges provided have a wrong format, privileges must be the format {'roles': ['role_id'], 'permissions':['permission_id']} as a dictionary")

    if not isinstance(request.Privileges['roles'], list):
        raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                            detail="the privileges provided have a wrong format, permissions and roles must be of type list")

    if not isinstance(request.Privileges['permissions'], list):
        raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                            detail="the privileges provided have a wrong format, permissions and roles must be of type list")


    # get  the current datetime
    current_date_time = datetime.now()

    # convert datetime to string format %Y/%m/%d %H:%M:%S
    privilege_updated_at = current_date_time.strftime('%Y-%m-%d %H:%M:%S')

    student.Privileges = request.Privileges
    student.Updated_at = privilege_updated_at
    db.session.commit()

    return {
        'message': f'student {request.SID} privileges updated successfully'
    }


def update_student_enrollment(request, user_id) -> dict:

    student = db.session.query(models.StudentEnrollment).filter(models.StudentEnrollment.SID == request.SID).first()

    if not student:
        raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                            detail=f"can not find student {request.SID} enrollment record")

    # get  the current datetime
    current_date_time = datetime.now()

    # convert datetime to string format %Y/%m/%d %H:%M:%S
    enrollment_updated_at = current_date_time.strftime('%Y-%m-%d %H:%M:%S')

    student.SCID = request.SCID
    student.Enrolled_By = request.Enrolled_By
    student.Updated_at = enrollment_updated_at
    db.session.commit()

    return {
        'message': 'student enrollment updated successfully'
    }


def create_user_profile(request, user_id) -> dict:
    user = db.session.query(models.Users).filter(
        and_(
            models.Users.First_Name == request.First_Name,
            models.Users.Last_Name == request.Last_Name
        )).first()

    if user:
        raise HTTPException(status_code=403, detail=f'User already exists')

        # generate a random user id for new student
    generated_user_id = generator_id('UID')

    # handle errors from generating user id
    if generated_user_id != 'GIDERR00' or generated_user_id != 'GIDERR01':

        first_name = request.First_Name.capitalize()
        last_name = request.Last_Name.capitalize()
        gender = request.Gender.capitalize()
        dob = request.DOB
        address = request.Address.capitalize()
        cell_number = request.Cell_Number.capitalize()


        # validate DOB date format
        try:
            bool(datetime.strptime(request.DOB, '%Y-%m-%d'))
        except ValueError:
            raise HTTPException(status_code=403, detail=f'DOB format not correct. Try Y-m-d')

        # check if the first name contains any numbers
        if has_numbers(first_name):
            raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                                detail="first name can not contains numbers")

        # check if the last name contains any numbers
        if has_numbers(last_name):
            raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                                detail="last name can not contains numbers")

        # check if the gender contains any numbers
        if has_numbers(gender):
            raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                                detail="gender can not contains numbers")

        # validate gender to come as a single letter
        if len(gender) > 1:
            raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                                detail="gender can either be M or F")

        # check if the DOB contains any letters
        if not re.search(r"[A-Z a-z]", dob) is None:
            raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                                detail="DOB can not contains letters")

        # check if the all cell number have 12 digits
        if len(cell_number) != 12:
            raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                                detail="all cell numbers must be 12 characters starting with 263")

        # check if the guardian_cell_number contains any letters or special characters
        if not re.search(r"[ !@#$%&'()*+,-./[\\\]^_`{|}~A-Za-z" + r'"]', cell_number) is None:
            raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                                detail="user cell number can not contains other characters")

        # check if the student_cell_number begin with 263
        if cell_number[:3] != '263':
            raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                                detail="all cell numbers must begin with 263")

    # get  the current datetime
    current_date_time = datetime.now()

    # convert datetime to string format %Y/%m/%d %H:%M:%S
    user_created_at = current_date_time.strftime('%Y-%m-%d %H:%M:%S')

    # create new student in db
    new_user = models.Users(
        UID=generated_user_id,
        First_Name=first_name,
        Last_Name=last_name,
        Gender=gender,
        DOB=dob,
        Address=address,
        Cell_Number=cell_number,
        Created_at=user_created_at,
        Updated_at='Null',
        Deleted_at='Null',
        Password='Default'
    )

    # add new student in db
    db.session.add(new_user)

    # commit new student (True = error, False = success)
    if db.session.commit():
        raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                            detail="there was an error creating the student record")

    # generate a new privilege id for the student
    privilege_id = generator_id('PHID')


    role = db.session.query(models.Roles).filter(
            models.Roles.RID == request.Role_Id
        ).first()

    if not role:
        user_role = 'Default'
    else:
        user_role = request.Role_Id


    # create new privilege in db
    new_user_privilege = models.PrivilegeHandler(
        PHID=privilege_id,
        Privilege=json.dumps({"roles": [user_role], "permissions": request.Permissions, "hold_response": "HRID00"}),
        UID=generated_user_id,
        Created_at=user_created_at,
        Updated_at='Null',
        Deleted_at='Null'
    )

    # add new privilege in db
    db.session.add(new_user_privilege)

    # commit new privilege
    if db.session.commit():
        raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                            detail="there was an error creating the user privileges")

    # generate a new hold response id for the student
    hold_response_id = generator_id('HRHID')

    # create new hold response in db
    new_user_hold_response = models.HoldResponseHandler(
        HRHID=hold_response_id,
        HR_CODE=json.dumps(['00']),
        UID=generated_user_id,
        Created_at=user_created_at,
        Updated_at='Null',
        Deleted_at='Null'
    )
    # add new hold responses in db
    db.session.add(new_user_hold_response)

    # commit new hold response
    if db.session.commit():
        raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                            detail="there was an error creating the user hold response")

    # the organisation id the user is being enrolled into
    organisation_enrolled_id = db.session.query(models.Organisations).filter(
        models.Organisations.OID == request.Organisation_id
    ).first()

    if not organisation_enrolled_id:
        oid = 'Default'
    else:
        oid = organisation_enrolled_id.OID

    # generate a new enrollment id for the student
    enrollment_id = generator_id('UEID')

    # create enrollment in db
    new_enrollment = models.UserEnrollment(
        UEID=enrollment_id,
        UID=generated_user_id,
        OID=oid,
        Enrolled_By=user_id,
        Created_at=user_created_at,
        Updated_at='Null',
        Deleted_at='Null'
    )

    # add new enrollment in db
    db.session.add(new_enrollment)

    # commit new enrollment
    if db.session.commit():
        raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                            detail="there was an error creating the user enrollment record")

    return {
        'message': 'user record created successfully',
    }



async def bulk_insert_student_marks(file, user_id):
    # Check whether the specified
    # path exists or not
    doesDirectoryExist = os.path.exists(f'uploads/{user_id}')

    if not doesDirectoryExist:
        os.mkdir(f'uploads/{user_id}')

    path = f'uploads/{user_id}'
    current_date_time = datetime.now()
    file_created_at = current_date_time.strftime('%Y%m%d%H%M%S')

    file_location = f"{path}/{file_created_at} {file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())
    print({"info": f"file '{file.filename}' saved at {file_location}"})

    job_created_at = current_date_time.strftime('%Y-%m-%d %H:%M:%S')

    new_job = models.GradeWorker(

        File_path=f'../{file_location}',
        Uploaded_by=user_id,
        Status='pending',
        Info='Null',
        Created_at=job_created_at,
        Updated_at='Null',
        Deleted_at='Null',
    )

    # add new student in db
    db.session.add(new_job)

    db.session.commit()


    return {
        'message': 'file uploaded successfully',
        'process_status': 'visit http://127.0.0.1:8000/user/upload/check_bulk_upload_status to check your upload status',

    }


def check_bulk_upload_status(user_id):
    jobs = db.session.query(models.GradeWorker).filter(
        models.GradeWorker.Status == 'processed',
        models.GradeWorker.Uploaded_by == user_id,
    ).order_by(models.GradeWorker.ID.desc()).limit(3)

    if not jobs:
        raise HTTPException(status_code=status.HTTP_206_PARTIAL_CONTENT,
                            detail="you do not have any pending uploads")

    job_status = {}

    loop_count = 1

    job_status[f'information'] = 'Retrieved the latest 3 uploads'


    for job in jobs:
        split_path = job.File_path.split('/')
        job_status[f'upload {loop_count}'] = {'file': split_path[3],
                                              'status': job.Status,
                                              'skipped': json.loads(job.Info)
                                              }
        loop_count += 1


        #print(job.ID)
    # print(job_status)
    return job_status




def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)
