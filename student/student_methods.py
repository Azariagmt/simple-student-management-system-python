from db import school_DBMS
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

    studentObject = studentLogic.Student(**newStudentData)

    print(f"""
                    Verify student Data

        First Name    = {studentObject.getFirstName()}
        Last Name     = {studentObject.getLastName()}
        Gender        = {studentObject.getGender()}
        Date of Birth = {studentObject.getDateOfBirth()}

    """)

    response = input("yes to enter student to DB \n")
    if response.upper() == 'YES':
        school_DBMS.addStudent(**newStudentData)


def updateStudent():
    name = input('Search first name\n')
    print(f"""
    Search results for {name}: \n
    """)
    school_DBMS.selectStudent(name=name)
    selectedId = int(input('Select Id of student you want to update'))
    result = []
    result = school_DBMS.selectStudent(selectedId=selectedId)
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

    oldStudentObject = studentLogic.Student(**tobeUpdatedStudentData)
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

        studentObject = studentLogic.Student(**newStudentData)

        print(f"""
                        Verify student Data

            First Name    = {studentObject.getFirstName()}
            Last Name     = {studentObject.getLastName()}
            Gender        = {studentObject.getGender()}
            Date of Birth = {studentObject.getDateOfBirth()}

        """)

        school_DBMS.updateStudent(**newStudentData)
        print('success editing student')


def readAllStudents():
    while True:
        school_DBMS.readAllStudents()
        x = int(input(' press 0 to go back home \n'))
        if x == 0:
            break


def deleteStudent():
    name = input('Search first name\n')
    print(f"""
    Search results for {name}: \n
    """)
    school_DBMS.selectStudent(name=name)
    selectedId = int(input('Select Id of student you want to update'))
    result = []
    result = school_DBMS.selectStudent(selectedId=selectedId)
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

    tobeDeletedStudentObject = studentLogic.Student(**tobeDeletedStudentData)
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
        school_DBMS.deleteStudent(selectedId=selectedId)
