from student import student_home
from student import student_login
import sqlite3

# create database and connect

db = sqlite3.connect('school-DBMS.db')
cur = db.cursor()

# create queries


def createTables():
    cur.execute("DROP TABLE IF EXISTS school")
    cur.execute("DROP TABLE IF EXISTS class")
    cur.execute("DROP TABLE IF EXISTS teacher")
    cur.execute("DROP TABLE IF EXISTS student")
    cur.execute("""
    CREATE TABLE school(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(40)
    );
    """)
    cur.execute("""
     CREATE TABLE class(
        id INT(5),
        name VARCHAR(2),
        school_id INT(5)
    );
    """)
    cur.execute("""
    CREATE TABLE student(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name VARCHAR(16),
        last_name VARCHAR(16),
        username VARCHAR(16),
        password VARCHAR(16),
        gender VARCHAR(1),
        date_of_birth DATE,
        date_of_enrollment DATE,
        security_question VARCHAR(30),
        security_answer VARCHAR(30)
    );
    """)
    print('success')


# query to add student into db
def addStudent(**kwargs):
    cur.execute(f"""
        INSERT INTO student (first_name, last_name, gender , date_of_birth, date_of_enrollment)
        VALUES('{kwargs['firstName']}','{kwargs['lastName']}','{kwargs['gender']}','{kwargs['dOB']}', '{kwargs['dOE']}');
        """)
    db.commit()

# read queries


def readAllStudents():
    for row in cur.execute("SELECT * FROM student;"):
        print(row)


def selectStudent(name=None, selectedId=None):
    if name:
        results = cur.execute(f"""
        SELECT * FROM student
        WHERE first_name = '{name}';
        """)
        for row in results:
            print(f'{row}')
    elif selectedId:
        results = cur.execute(f"""
        SELECT * FROM student
        WHERE id = '{selectedId}';
        """)
        for row in results:
            print(f'{row}')
            return row

    return

# update


def updateStudent(**kwargs):
    cur.execute(f"""
    UPDATE student
    SET first_name = '{kwargs['firstName']}',last_name = '{kwargs['lastName']}',gender = '{kwargs['gender']}',date_of_birth = '{kwargs['dOB']}', date_of_enrollment = '{kwargs['dOE']}'
    WHERE id = {kwargs['selectedId']}; 
    """)
    db.commit()
# delete


def deleteStudent(selectedId=None):
    if selectedId:
        cur.execute(f"""
        DELETE FROM student WHERE id = {selectedId};
        """)
        db.commit()


def verifyStudent(name=None, password=None):
    if name and password:
        results = cur.execute(f"""
        SELECT * FROM student 
        WHERE name = '{name}' AND password = '{password}
        """)
        if results:
            for row in results:
                return row
        else:
            login.choice()
    elif name:
        results = cur.execute(f"""
        SELECT * FROM student
        WHERE name = {name}
        """)
        if results:
            for row in results:
                return row
        else:
            return f'no name found'


def changePassword(name):
    results = verifyStudent(name=name)
    for result in results:
        print(result)
    selected_id = input('select your id!')
    if fetch_security_question(selected_id):
        newPassword = input('Please enter new password \n')
        confirmPassword = input('confirm password')
        if newPassword == confirmPassword:
            cur.execute(f"""
                    ALTER TABLE STUDENT 
                    SET password = {newPassword}
                    WHERE id = {selected_id};
                    """)
            print('Password changed successfully')


def fetch_security_question(selected_id):
    question = cur.execute(f"""
    SELECT security_question FROM student 
    WHERE id = {selected_id}
    """)
    answer = cur.execute(f"""
    SELECT security_answer FROM student 
    WHERE id = {selected_id}
    """)
    print([question for question in question])
    guess = input('Input answer for security question..\n')

    if guess == answer:
        return True


if __name__ == "__main__":
    createTables()
