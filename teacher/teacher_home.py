from teacher import teacher_methods


def teacher_home(*args):
    print(args)
    while True:
        print("""
        welcome teacher

        what u wanna do?

        1. grade student
        2. set security question....

        """)
        choice = int(input('what u wanna do? \n'))
        if choice == 1:
            teacher_methods.grade_student(args[0])
