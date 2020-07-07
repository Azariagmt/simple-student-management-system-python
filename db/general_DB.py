import sqlite3
from teacher import teacher_login
from teacher import teacher_home
from student import student_login
from student import student_home
from admin import admin_login
from admin import admin_home

db = sqlite3.connect('school-DBMS.db')
cur = db.cursor()


def verify_credentials(username=None, password=None, entity=None):
    if entity == 'teacher' and username and password:
        result = cur.execute(f"""
            SELECT * FROM teacher 
            WHERE username = '{username}' 
            AND password = '{password}' 
        """)
        if result:
            teacher_home.teacher_home(result)
        else:
            print("no result found")
            teacher_login.login()
    elif entity == 'student' and username and password:
        result = cur.execute(f"""
        SELECT * FROM student 
        WHERE username = '{username}' 
        AND password = '{password}';
        """)
        if result:
            print(result)
            student_home.student_home(result)
        else:
            print("no result found")
            student_login.login()
    elif entity == 'admin' and username and password:
        result = cur.execute(f"""
        SELECT * FROM admin
        WHERE username = '{username}'
        AND password = '{password}'
        """)
        if result:
            admin_home.admin_home(result)
        else:
            print("no result found")
            admin_login.login()
    elif username and entity:
        result = cur.execute(f"""
        SELECT * FROM {entity}
        WHERE username = '{username}'
        """)
        return result
    else:
        print('error')


def changePassword(name, entity):
    results = verify_credentials(username=name, entity=entity)
    for result in results:
        print(result)
    selected_id = input('select your id!')
    if fetch_security_question(selected_id, entity=entity):
        newPassword = input('Please enter new password \n')
        confirmPassword = input('confirm password')
        if newPassword == confirmPassword:
            cur.execute(f"""
                    ALTER TABLE {entity}
                    SET password = {newPassword}
                    WHERE id = {selected_id};
                    """)
            print('Password changed successfully')


def fetch_security_question(selected_id, entity):
    question = cur.execute(f"""
    SELECT security_question FROM {entity} 
    WHERE id = {selected_id};
    """)
    answer = cur.execute(f"""
    SELECT security_answer FROM {entity} 
    WHERE id = {selected_id};
    """)
    print([question for question in question])
    guess = input('Input answer for security question..\n')

    if guess == answer:
        return True
