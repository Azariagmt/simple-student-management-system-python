from db import school_DBMS


def login():
    print("""
    
    Login to your account!

        other: forgot/change password? 1
               Go back to home? 0
    
    """)
    name = input('Enter username')
    password = input('Enter password \n ')

    if password == '1' or name == '1':
        change_password()
    elif name == '0' or password == '1':
        pass
    else:
        school_DBMS.verifyStudent()


def change_password():
    tochange_name = input('enter firstname or username')
    school_DBMS.changePassword(tochange_name)
