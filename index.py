import utilities
from teacher import teacher_login
from admin import admin_login

from student import student_login
from db import general_DB


def main():
    homePage()


def homePage():
    while True:
        utilities.clear()
        print("""

        (```````````````````````````````````````````````````````````)
        (              BLaBla UNIVESITY PORTAL                      )
        (               how do u wanna login as?                    )
        (                                                           )
        (         1.  Student                                       )
        (         2.  Teacher                                       )
        (         3.  Admin                                         )
        (         000.Reset password                                )
        (_________0.  exit__________________________________________)

        """)

        choice = int(input('Please make a choice. \n'))

        if choice == 1:
            student_login.login()
        elif choice == 2:
            teacher_login.login()
        elif choice == 3:
            admin_login.login()
        elif choice == 000:
            # reset password link
            utilities.clear()
            print("""
            What are you?
            1. Student
            2. Teacher
            3. Admin
            4. Robot
            """)
            selection = int(input('what are you? \n'))
            if selection == 1:
                selection = 'student'
            elif selection == 2:
                selection = 'teacher'
            elif selection == 3:
                selection = 'admin'
            else:
                print('idkkkkk and idc')
                continue
            username = input('Enter your username \n')
            general_DB.changePassword(username, selection)
        elif choice == 0:
            utilities.clear()
            print("exiting...")
            break
        else:
            print('Error please enter choice again!')


main()
