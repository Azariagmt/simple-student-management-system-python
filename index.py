import utilities
from student import student_login
from teacher import teacher_login
from admin import admin_login


def main():
    homePage()


def homePage():
    utilities.clear()
    while True:
        print("""

        (```````````````````````````````````````````````````````````)
        (              BLaBla UNIVESITY PORTAL                      )
        (               how do u wanna login as?                    )
        (                                                           )
        (         1.Student                                         )
        (         2.Teacher                                         )
        (         3.Admin                                           )
        (         000.reset password                                )
        (_________0.exit____________________________________________)

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
            pass
        elif choice == 0:
            print("exiting...")
            break
        else:
            print('Error please enter choice again!')


main()
