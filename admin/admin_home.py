import utilities
from db import student_DB
from admin import admin_methods


def admin_home(*args):
    '''
    admin db credentials not showing up
    '''
    utilities.clear()
    for row in args:
        for user in row:
            print(f'{user}')

    while True:
        print(f"""
        welcome to home page of admin
    

        what do you wanna do?
        1. View all students
        2. view single student info
        3. enter new student
        4. Delete student
        """)

        choice = int(input('Enter choice'))

        if choice == 1:
            student_DB.readAllStudents()
        elif choice == 2:
            while True:
                print("""
                how do you wanna search?
                1. by id
                2. by name 
                """)
                select = int(input("how u wanna search?"))
                if select == 1:
                    selected_id = int(input('Enter Id'))
                    student_DB.selectStudent(selectedId=selected_id)
                elif select == 2:
                    name = input('enter student name')
                    student_DB.selectStudent(name)
                else:
                    continue
        elif choice == 3:
            utilities.clear()
            print("""
            Entering new student data
            """)
            admin_methods.createStudent()
            student_DB.addStudent()
        elif choice == 4:
            print("""
            Proceed with caution!
            Deleting student data...
            """)
            selected_id = input('enter student id to delete')
            student_DB.deleteStudent(selectedId=selected_id)
