import sqlite3

db = sqlite3.connect('school-DBMS.db')
cur = db.cursor()

# query to add student into db


def addStudent(**kwargs):
    cur.execute(f"""
        INSERT INTO student(first_name, last_name, username, password, gender , date_of_birth, date_of_enrollment)
        VALUES(
        '{kwargs['firstName']}',
        '{kwargs['lastName']}',
        '{kwargs['username']}',
        '{kwargs['password']}',
        '{kwargs['gender']}',
        '{kwargs['dOB']}', 
        '{kwargs['dOE']}');
        """)
    print('success inserting')
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
