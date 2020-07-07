import sqlite3
from admin import admin_home

db = sqlite3.connect('school-DBMS.db')
cur = db.cursor()

# create C


def add_teacher(**kwargs):
    cur.execute(f"""
    INSERT INTO teacher('first_name', 'last_name','username','password','gender', 'date_of_birth') 
    VALUES(
        '{kwargs['firstName']}',
        '{kwargs['lastName']}',
        '{kwargs['username']}',
        '{kwargs['password']}',
        '{kwargs['gender']}',
        '{kwargs['dOB']}'
    );    
    """)
    db.commit()

# read R


def read_all_teachers():
    return cur.execute("SELECT * FROM teacher")


def select_teacher(username=None, selected_id=None):
    if username:
        results = cur.execute(f"""
        SELECT * FROM teacher
        WHERE username = '{username}'
        """)
        for row in results:
            print(row)
        return results
    elif selected_id:
        results = cur.execute(f"""
        SELECT * FROM teacher
        WHERE id = '{selected_id}'        
        """)
        return results
    else:
        print('idk')


# delete D

def delete_teacher(selected_id=None):
    if selected_id:
        res = cur.execute(f"""
        SELECT * FROM teacher
        WHERE id = {selected_id};
        """)
        for row in res:
            print(row)
            print('You about to delete the above data...')
            proceed = input('Yes to proceed \n')
            if proceed.upper() == 'YES':
                result = cur.execute(f"""
                DELETE FROM teacher 
                WHERE id = {selected_id};
                """)
                if result:
                    db.commit()
            else:
                delete_teacher()
    else:
        admin_home.admin_home()


#update U

def update_teacher(**kwargs):
    cur.execute(f"""
    UPDATE teacher
    SET first_name = '{kwargs['firstName']}',last_name = '{kwargs['lastName']}',gender = '{kwargs['gender']}',date_of_birth = '{kwargs['dOB']}', date_of_enrollment = '{kwargs['dOE']}'
    WHERE id = {kwargs['selectedId']}; 
    """)
    db.commit()