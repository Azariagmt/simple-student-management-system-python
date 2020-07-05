import utilities
from student import student_login


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
        (                                                           )
        (___________________________________________________________)

        """)

        choice = int(input('Please make a choice. \n'))

        if choice == 1:
            student_login.choose()
        else:
            print('Error please enter choice again!')


main()
