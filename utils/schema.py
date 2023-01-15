from typing import Optional
from pydantic import BaseModel


class StudentInfo(BaseModel):
    SID: str
    fullname: str
    gender: str
    token: str


class CreateStudent(BaseModel):
    First_Name: str
    Last_Name: str
    Gender: str
    DOB: str
    Address: str
    Guardian_Full_Name: str
    Guardian_Cell_Number: str
    Student_Cell_Number: str
    School_enrolled: str


class UserLogin(BaseModel):
    UserID: str
    Password: str


class Grades(BaseModel):
    ID: int
    GID: str
    UID: str
    SID: str
    SCID: str
    Marks_By_Subject: str
    Term: str
    Level: str
    Percentage: str
    Grading_schema: str
    Created_at: str
    Updated_at: str
    Deleted_at: str


class TokenData(BaseModel):
    token_otp: Optional[str] = None


class UpdateStudentHoldResponse(BaseModel):
    SID: str
    HRID: str


class UpdateStudentPrivileges(BaseModel):
    SID: str
    Privileges: dict


class UpdateStudentEnrollment(BaseModel):
    SID: str
    SCID: str
    Enrolled_By: str

class CheckBulkUploadStatus(BaseModel):
    UID: str


class CreateUser(BaseModel):
    First_Name: str
    Last_Name: str
    Gender: str
    DOB: str
    Address: str
    Cell_Number: str
    Organisation_id: str
    Role_Id: str
    Permissions: list
