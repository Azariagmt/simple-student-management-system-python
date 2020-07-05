import utilities
from db import student_DB
from student import student_logic


def readAllStudents():
    while True:
        student_DB.readAllStudents()
        x = int(input(' press 0 to go back home \n'))
        if x == 0:
            break


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
