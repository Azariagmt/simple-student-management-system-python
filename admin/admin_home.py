import utilities


def admin_home(*args):
    '''
    admin db credentials not showing up
    '''
    utilities.clear()
    for row in args:
        for user in row:
            print(user)
    print(f"""
        welcome to home page of admin
    

        what do you wanna do?
        1. View all students
        2. Delete student
    """)

    choice = input('Enter choice')
