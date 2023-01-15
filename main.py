"""
Modules used in the application
"""
import json
import uvicorn
from fastapi import FastAPI, Request, UploadFile
from utils import schema, functions

app = FastAPI()


@app.get('/')
async def fetch():
    """
    Default route showing API greeting message.
    """
    return {
        'message': 'Welcome to Zim School API'
    }


@app.get('/student/login')
async def student_login():
    """
    Login route for students to get token that enables them to access other routes
    """

    login_data = functions.student_login('SID00001', '123456')

    parsed_data = json.loads(login_data)

    return {
        'SID': parsed_data['SID'],
        'Fullname': parsed_data['Fullname'],
        'Gender': parsed_data['Gender'],
        'Token': parsed_data['Token'],
    }


@app.post('/student/myinfo')
async def student_info(request: schema.StudentInfo):
    """
    Route for students which returns information for a particular logged in students
    """

    # verify token and access rights
    student_id = functions.verify_token(request.token,
                                        {'required_permissions': ['PID00003'], 'required_roles': ['RID00004']})

    student_data = functions.student_get_info(student_id)
    parsed_student_info = json.loads(student_data)
    return {
        'Name': parsed_student_info['Name'],
        'Surname': parsed_student_info['Surname'],
        'Gender': parsed_student_info['Gender'],
        'DOB': parsed_student_info['DOB'],
        'Address': parsed_student_info['Address'],
        'Phone_number': parsed_student_info['Phone_number'],
        'Guardian': parsed_student_info['Guardian'],
        'Guardian_phone_number': parsed_student_info['Guardian_phone_number'],
        'Grades': parsed_student_info['Grades'],
        'Enrolled_schools': parsed_student_info['Enrolled_schools']
    }


@app.post('/user/login')
async def user_login(request: schema.UserLogin):
    login_data = functions.user_login(request.UserID, request.Password)

    parsed_data = json.loads(login_data)

    return {
        'UID': parsed_data['UID'],
        'Fullname': parsed_data['Fullname'],
        'Gender': parsed_data['Gender'],
        'Token': parsed_data['Token'],
    }


@app.get('/user/search/{data_to_search}')
async def user_update(request: Request, search: str):
    user_token = functions.verify_headers(request)

    user_id = functions.verify_token(user_token,
                                     {
                                         'required_permissions': ['PID00002'],
                                         'required_roles': ['RID00002']
                                     })

    result = functions.search_student(search)

    return result


@app.post('/user/create/student_profile')
async def user_login(request: schema.CreateStudent, request_headers: Request):
    user_token = functions.verify_headers(request_headers)

    user_id = functions.verify_token(user_token,
                                     {
                                         'required_permissions': ['PID00001'],
                                         'required_roles': ['RID00001']
                                     })

    creation_response = functions.create_student_profile(request, user_id)

    return creation_response


@app.post('/user/update/student_info')
async def user_login(request: schema.CreateStudent, request_headers: Request):
    user_token = functions.verify_headers(request_headers)

    user_id = functions.verify_token(user_token,
                                     {
                                         'required_permissions': ['PID00001'],
                                         'required_roles': ['RID00001']
                                     })

    return ''


@app.post('/user/update/student_hold_response')
async def student_hold_response(request: schema.UpdateStudentHoldResponse, request_headers: Request):
    user_token = functions.verify_headers(request_headers)

    user_id = functions.verify_token(user_token,
                                     {
                                         'required_permissions': ['PID00015'],
                                         'required_roles': ['RID00001']
                                     })

    update_response = functions.update_hold_response(request, user_id)

    return update_response


@app.post('/user/update/student_privileges')
async def student_privileges(request: schema.UpdateStudentPrivileges, request_headers: Request):

    user_token = functions.verify_headers(request_headers)

    user_id = functions.verify_token(user_token,
                                     {
                                         'required_permissions': ['PID00011'],
                                         'required_roles': ['RID00001']
                                     })

    update_response = functions.update_student_privileges(request, user_id)

    return update_response


@app.post('/user/update/student_enrollment')
async def student_enrollment(request: schema.UpdateStudentEnrollment, request_headers: Request):

    user_token = functions.verify_headers(request_headers)

    user_id = functions.verify_token(user_token,
                                     {
                                         'required_permissions': ['PID00007'],
                                         'required_roles': ['RID00001']
                                     })

    update_response = functions.update_student_enrollment(request, user_id)

    return update_response


@app.post('/user/create/user')
async def student_enrollment(request: schema.CreateUser, request_headers: Request):

    user_token = functions.verify_headers(request_headers)

    user_id = functions.verify_token(user_token,
                                     {
                                         'required_permissions': ['PID00018', 'PID00022', 'PID00026', 'PID00030'],
                                         'required_roles': ['RID00001']
                                     })

    update_response = functions.create_user_profile(request, user_id)

    return update_response


@app.post('/user/upload/bulk_student_marks')
async def create_upload_file(file: UploadFile):
    # user_token = functions.verify_headers(request_headers)
    #
    # user_id = functions.verify_token(user_token,
    #                                  {
    #                                      'required_permissions': ['PID00018', 'PID00022', 'PID00026', 'PID00030'],
    #                                      'required_roles': ['RID00001']
    #                                  })

    upload_response = await functions.bulk_insert_student_marks(file, "UID00001")

    # contents = await file.read()

    print(upload_response)

    return {"filename": file.filename}



@app.post('/user/upload/check_bulk_upload_status')
async def check_bulk_upload_status(request: schema.CheckBulkUploadStatus):

    check_response =  functions.check_bulk_upload_status(request.UID)

    return check_response




if __name__ == '__main__':
    uvicorn.run(app)
