import utilities
from db import student_DB
from student import student_logic
from admin import admin_home
from teacher import teacher_logic
from db import teacher_DB

# read
def readAllStudents():
    while True:
        student_DB.readAllStudents()
        x = int(input(' press 0 to go back home \n'))
        if x == 0:
            break

# delete
def deleteStudent():
    name = input('Search first name\n')
    print(f"""
    Search results for {name}: \n
    """)
    student_DB.selectStudent(name=name)
    selectedId = int(input('Select Id of student you want to update'))
    result = []
    result = student_DB.selectStudent(selectedId=selectedId)
    print(f"""
    editing {result}
    """)
    tobeDeletedStudentData = {
        'firstName': result[0],
        'lastName': result[1],
        'dOB': result[3],
        'gender': result[2],
        'dOE': result[4],
        'selectedId': selectedId
    }

    tobeDeletedStudentObject = student_logic.Student(**tobeDeletedStudentData)
    print(f"""
                    Verify student Data
        You are deleting student

        First Name    = {tobeDeletedStudentObject.getFirstName()}
        Last Name     = {tobeDeletedStudentObject.getLastName()}
        Gender        = {tobeDeletedStudentObject.getGender()}
        Date of Birth = {tobeDeletedStudentObject.getDateOfBirth()}

    """)
    cont = input('do you wish to proceed')
    if cont.upper() == 'YES':
        student_DB.deleteStudent(selectedId=selectedId)


# create
def createStudent():
    utilities.clear()
    print('creating student')
    firstName = input('Enter students first Name \n')
    lastName = input('Enter students last Name \n')
    gender = input('Enter Gender\n')
    dateOfBirth = input('Enter date of birth\n')
    dateOfEnrollment = input('Enter date of enrollment\n')

    newStudentData = {
        'firstName': firstName,
        'lastName': lastName,
        'dOB': dateOfBirth,
        'gender': gender,
        'dOE': dateOfEnrollment
    }

    studentObject = student_logic.Student(**newStudentData)

    print(f"""
                    Verify student Data

        First Name    = {studentObject.getFirstName()}
        Last Name     = {studentObject.getLastName()}
        Gender        = {studentObject.getGender()}
        Date of Birth = {studentObject.getDateOfBirth()}

    """)

    newStudentData['username'] = studentObject.username
    newStudentData['password'] = studentObject.password

    response = input("yes to enter student to DB \n")
    if response.upper() == 'YES':
        student_DB.addStudent(**newStudentData)
        admin_home.admin_home({'name': 'admin'})


def create_teacher():
    utilities.clear()
    print("""
    Adding new teacher!!
    """)
    first_name = input('first name of teacher \n')
    last_name = input('last name of teacher \n')
    sex = input('Enter gender \n')
    dOB = input('Enter date of birth \n')

    new_teacher_data = {
        'firstName': first_name,
        'lastName': last_name,
        'gender': sex,
        'dOB': dOB
    }

    teacher_object = teacher_logic.Teacher(**new_teacher_data)

    print(f"""
    Verify data
        {teacher_object.getFirstName()}
        {teacher_object.getLastName()}
        {teacher_object.getGender()}
        {teacher_object.getDateOfBirth()}
    """)

    new_teacher_data['username'] = teacher_object.username
    new_teacher_data['password'] = teacher_object.password

    ver = input('ENter yes if data is correct')
    if ver.upper() == 'YES':
        teacher_DB.add_teacher(**new_teacher_data)


# update
def updateStudent():
    name = input('Search first name\n')
    print(f"""
    Search results for {name}: \n
    """)
    student_DB.selectStudent(name=name)
    selectedId = int(input('Select Id of student you want to update'))
    result = []
    result = student_DB.selectStudent(selectedId=selectedId)
    print(f"""
    editing {result}
    """)
    tobeUpdatedStudentData = {
        'firstName': result[0],
        'lastName': result[1],
        'dOB': result[3],
        'gender': result[2],
        'dOE': result[4]
    }

    oldStudentObject = student_logic.Student(**tobeUpdatedStudentData)
    print(f"""
                    Verify student Data
        You are editing

        First Name    = {oldStudentObject.getFirstName()}
        Last Name     = {oldStudentObject.getLastName()}
        Gender        = {oldStudentObject.getGender()}
        Date of Birth = {oldStudentObject.getDateOfBirth()}

    """)
    cont = input('do you wish to proceed')
    if cont.upper() == 'YES':
        firstName = input('Enter students first Name \n')
        lastName = input('Enter students last Name \n')
        gender = input('Enter Gender\n')
        dateOfBirth = input('Enter date of birth\n')
        dateOfEnrollment = input('Enter date of enrollment\n')

        newStudentData = {
            'firstName': firstName,
            'lastName': lastName,
            'dOB': dateOfBirth,
            'gender': gender,
            'dOE': dateOfEnrollment,
            'selectedId': selectedId
        }

        studentObject = student_logic.Student(**newStudentData)

        print(f"""
                        Verify student Data

            First Name    = {studentObject.getFirstName()}
            Last Name     = {studentObject.getLastName()}
            Gender        = {studentObject.getGender()}
            Date of Birth = {studentObject.getDateOfBirth()}

        """)

        student_DB.updateStudent(**newStudentData)
        print('success editing student')
