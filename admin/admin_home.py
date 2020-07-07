import utilities
from db import student_DB
from admin import admin_methods
from db import teacher_DB


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
        2. View single student info
        3. Enter new student
        4. Delete student
        5. View all teachers
        6. View single teacher info
        7. Enter new teacher
        8. Delete teacher

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
        elif choice == 5:
            print("""
            view all teachers
            """)
            result = teacher_DB.read_all_teachers()
            for row in result:
                print(row)
        elif choice == 6:
            while True:
                print("""
                how do you wanna search?
                1. by id
                2. by name 
                """)
                select = int(input("how u wanna search?"))
                if select == 1:
                    selected_id = int(input('Enter Id'))
                    # student_DB.selectStudent(selectedId=selected_id)
                    result = teacher_DB.select_teacher(selected_id=selected_id)
                    for row in result:
                        print(row)
                elif select == 2:
                    name = input('enter teacher name')
                    # student_DB.selectStudent(name)
                    result = teacher_DB.select_teacher(name)
                    for row in result:
                        print(row)
                else:
                    continue
        elif choice == 7:
            utilities.clear()
            print("""
            Entering new teacher data
            """)
            admin_methods.create_teacher()
        elif choice == 8:
            utilities.clear()
            print("""
            proceed with caution about to delete teacher
            """)
            selected_id = input("enter id of teacher u wanna delete\n")
            teacher_DB.delete_teacher(selected_id)
