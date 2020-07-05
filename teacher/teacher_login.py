from db import general_DB
import utilities


def login():
    utilities.clear()
    print("""
    welcome teacher please enter credentials to login

    """)
    username = input('Enter username')
    password = input('Enter password \n enter 0 if forgot password(to reset)')

    general_DB.verify_credentials(username, password, 'teacher')
