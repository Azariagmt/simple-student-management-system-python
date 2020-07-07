from teacher import teacher_methods
import utilities

def teacher_home(*args):
    utilities.clear()
    for arg in args:
        for row in arg:
            print(row)
    while True:
        print("""
        welcome teacher

        what u wanna do?

        1. grade student
        2. set security question....
        3. change password
        0. exit
        """)
        choice = int(input('what u wanna do? \n'))
        if choice == 1:
            teacher_methods.grade_student(args[0])
        elif choice == 2:
            teacher_methods.set_security_question(args[0])
        elif choice == 3:
            teacher_methods.change_password(args[3])
        elif choice == 0:
            break
        else:
            print('didnt get that please try again...')
            continue
