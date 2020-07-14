
import utilities
from db import general_DB


def login():
    utilities.clear()
    print("""

    Login to your account!

    """)
    name = input('Enter username')
    password = input('Enter password \n')

    if name and password:
        general_DB.verify_credentials(
            username=name, password=password, entity='student')
    else:
        print("please enter username and password")


def change_password():
    tochange_name = input('enter firstname or username')
    general_DB.changePassword(tochange_name, 'student')
