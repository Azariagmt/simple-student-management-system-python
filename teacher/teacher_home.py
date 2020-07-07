from teacher import teacher_methods


def teacher_home(*args):
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

        """)
        choice = int(input('what u wanna do? \n'))
        if choice == 1:
            teacher_methods.grade_student(args[0])
        elif choice == 2:
            teacher_methods.set_security_question(args[0])
        elif choice == 3:
            teacher_methods.change_password(args[3])
