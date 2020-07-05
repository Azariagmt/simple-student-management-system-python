from db import general_DB


def login():
    print("""
    welcome teacher please enter credentials to login

    """)
    username = input('Enter username')
    password = input('Enter password \n enter 0 if forgot password(to reset)')

    general_DB.verify_credentials(username, password, 'teacher')
