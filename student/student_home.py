from student import student_methods
import index


def student_home(*args):
    while True:
        print(f"""
        
        welcome to your home page....what do you wanna do?
        {args[0]}

        1.View Grade
        2.View classes
        3.set security questions
        0.logout...
        """)
        choice = int(input('what u wanna do? \n'))
        if choice == 1:
            student_methods.view_grade()
        elif choice == 2:
            student_methods.view_classes()
        elif choice == 3:
            student_methods.set_security_question
        elif choice == 0:
            index.homePage()
        else:
            print('what?')
            continue
