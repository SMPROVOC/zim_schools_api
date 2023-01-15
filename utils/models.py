from sqlalchemy import Column, Integer, String, and_, or_, not_
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class PrivilegeHandler(Base):
    __tablename__ = "privilegehandler"
    ID = Column(Integer, primary_key=True, index=True, unique=True)
    PHID = Column(String(255), unique=True, nullable=False)
    Privilege = Column(String(255), nullable=False)
    UID = Column(String(255), nullable=False)
    Created_at = Column(String(255), nullable=False)
    Updated_at = Column(String(255), nullable=False)
    Deleted_at = Column(String(255), nullable=False)

class Roles(Base):
    __tablename__ = "roles"
    ID = Column(Integer, primary_key=True, index=True, unique=True)
    RID = Column(String(255), unique=True, nullable=False)
    Name = Column(String(255), nullable=False)
    Created_at = Column(String(255), nullable=False)
    Updated_at = Column(String(255), nullable=False)
    Deleted_at = Column(String(255), nullable=False)


class Subjects(Base):
    __tablename__ = "subjects"
    ID = Column(Integer, primary_key=True, index=True, unique=True)
    SUBID = Column(String(255), unique=True, nullable=False)
    Name = Column(String(255), nullable=False)
    Level = Column(String(255), nullable=False)
    Board = Column(String(255), nullable=False)
    Exam_Code = Column(String(255), nullable=False)
    Created_at = Column(String(255), nullable=False)
    Updated_at = Column(String(255), nullable=False)
    Deleted_at = Column(String(255), nullable=False)

class GradeWorker(Base):
    __tablename__ = "gradesworker"
    ID = Column(Integer, primary_key=True, index=True, unique=True)
    File_path = Column(String(255), nullable=False)
    Uploaded_by = Column(String(255), nullable=False)
    Status = Column(String(255), nullable=False)
    Info = Column(String(255), nullable=False)
    Created_at = Column(String(255), nullable=False)
    Updated_at = Column(String(255), nullable=False)
    Deleted_at = Column(String(255), nullable=False)

class GradingStructure(Base):
    __tablename__ = "gradingstructure"
    ID = Column(Integer, primary_key=True, index=True, unique=True)
    GSID = Column(String(255), nullable=False, unique=True)
    Name = Column(String(255), nullable=False)
    Structure = Column(String(255), nullable=False)
    Created_at = Column(String(255), nullable=False)
    Updated_at = Column(String(255), nullable=False)
    Deleted_at = Column(String(255), nullable=False)


class Organisations(Base):
    __tablename__ = "organisations"
    ID = Column(Integer, primary_key=True, index=True, unique=True)
    OID = Column(String(255), unique=True, nullable=False)
    Name = Column(String(255), nullable=False)
    Created_at = Column(String(255), nullable=False)
    Updated_at = Column(String(255), nullable=False)
    Deleted_at = Column(String(255), nullable=False)

class HoldResponseHandler(Base):
    __tablename__ = "holdresponsehandler"
    ID = Column(Integer, primary_key=True, index=True, unique=True)
    HRHID = Column(String(255), unique=True, nullable=False)
    HR_CODE = Column(String(255), nullable=False)
    UID = Column(String(255), nullable=False)
    Created_at = Column(String(255), nullable=False)
    Updated_at = Column(String(255), nullable=False)
    Deleted_at = Column(String(255), nullable=False)

class HoldResponses(Base):
    __tablename__ = "holdresponse"
    ID = Column(Integer, primary_key=True, index=True, unique=True)
    HRID = Column(String(255), unique=True, nullable=False)
    HR_CODE = Column(String(255), nullable=False)
    Description = Column(String(255), nullable=False)
    Created_at = Column(String(255), nullable=False)
    Updated_at = Column(String(255), nullable=False)
    Deleted_at = Column(String(255), nullable=False)


class Student(Base):
    __tablename__ = "students"

    ID = Column(Integer, primary_key=True, index=True, unique=True)
    SID = Column(String(255), unique=True, nullable=False)
    First_Name = Column(String(255), nullable=False)
    Last_Name = Column(String(255), nullable=False)
    Gender = Column(String(255), nullable=False)
    DOB = Column(String(255), nullable=False)
    Address = Column(String(255), nullable=False)
    Guardian_Full_Name = Column(String(255), nullable=False)
    Guardian_Cell_Number = Column(String(255), nullable=False)
    Student_Cell_Number = Column(String(255), nullable=False)
    Created_at = Column(String(255), nullable=False)
    Updated_at = Column(String(255), nullable=False)
    Deleted_at = Column(String(255), nullable=False)
    Password = Column(String(255))
    Hold_response = Column(String(255))


class Grades(Base):
    __tablename__ = "grades"
    ID = Column(Integer, primary_key=True, index=True, unique=True)
    GID = Column(String(255), unique=True, nullable=False)
    UID = Column(String(255), nullable=False)
    SID = Column(String(255), nullable=False)
    SCID = Column(String(255), nullable=False)
    Marks_By_Subject = Column(String(255), nullable=False)
    Term = Column(String(255), nullable=False)
    Level = Column(String(255), nullable=False)
    Percentage = Column(String(255), nullable=False)
    Grading_structure = Column(String(255), nullable=False)
    Created_at = Column(String(255), nullable=False)
    Updated_at = Column(String(255), nullable=False)
    Deleted_at = Column(String(255), nullable=False)


class StudentEnrollment(Base):
    __tablename__ = "studentenrollment"
    ID = Column(Integer, primary_key=True, index=True, unique=True)
    SEID = Column(String(255), unique=True, nullable=False)
    SID = Column(String(255), nullable=False)
    SCID = Column(String(255), nullable=False)
    Enrolled_By = Column(String(255), nullable=False)
    Created_at = Column(String(255), nullable=False)
    Updated_at = Column(String(255), nullable=False)
    Deleted_at = Column(String(255), nullable=False)


class UserEnrollment(Base):
    __tablename__ = "userenrollment"
    ID = Column(Integer, primary_key=True, index=True, unique=True)
    UEID = Column(String(255), unique=True, nullable=False)
    UID = Column(String(255), nullable=False)
    OID = Column(String(255), nullable=False)
    Enrolled_By = Column(String(255), nullable=False)
    Created_at = Column(String(255), nullable=False)
    Updated_at = Column(String(255), nullable=False)
    Deleted_at = Column(String(255), nullable=False)

class Users(Base):
    __tablename__ = "user_info"
    ID = Column(Integer, primary_key=True, index=True, unique=True)
    UID = Column(String(255), unique=True, nullable=False)
    First_Name = Column(String(255), nullable=False)
    Last_Name = Column(String(255), nullable=False)
    Gender = Column(String(255), nullable=False)
    DOB = Column(String(255), nullable=False)
    Address = Column(String(255), nullable=False)
    Cell_Number = Column(String(255), nullable=False)
    Password = Column(String(255))
    Created_at = Column(String(255), nullable=False)
    Updated_at = Column(String(255), nullable=False)
    Deleted_at = Column(String(255), nullable=False)


class School(Base):
    __tablename__ = "schools"
    ID = Column(Integer, primary_key=True, index=True, unique=True)
    SCID = Column(Integer, primary_key=True, unique=True)
    Name = Column(String(255), nullable=False)
    Province= Column(String(255), nullable=False)
    Motto = Column(String(255), nullable=False)
    Denomination = Column(String(255), nullable=False)
    Founded = Column(String(255), nullable=False)
    Authority = Column(String(255), nullable=False)
    Gender = Column(String(255), nullable=False)
    Average_class_size = Column(String(255), nullable=False)
    Classes_offered = Column(String(255), nullable=False)
    Languages = Column(String(255), nullable=False)
    Colors = Column(String(255), nullable=False)
    Slogan = Column(String(255), nullable=False)
    Sports = Column(String(255), nullable=False)
    Nickname = Column(String(255), nullable=False)
    Coordinates = Column(String(255), nullable=False)
    Address = Column(String(255), nullable=False)
    Badge = Column(String(255), nullable=False)
    Is_boarding = Column(String(255), nullable=False)
    Created_at = Column(String(255), nullable=False)
    Updated_at = Column(String(255), nullable=False)
    Deleted_at= Column(String(255), nullable=False)