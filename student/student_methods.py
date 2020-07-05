from db import school_DBMS
from db import student_DB
from datetime import date
import utilities
from student import student_logic


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

    response = input("yes to enter student to DB \n")
    if response.upper() == 'YES':
        student_DB.addStudent(**newStudentData)


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
