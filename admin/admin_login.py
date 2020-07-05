from db import general_DB


def login():
    print(f"""
    
    Welcome admin enter username and password 

    """)
    name = input('Enter username \n')
    password = input('Enter password \n')

    if name and password:
        general_DB.verify_credentials(
            username=name, password=password, entity='admin'
        )
    else:
        print("Please enter username and password")
        login()
