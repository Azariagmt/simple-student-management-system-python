import sqlite3

# create database and connect

db = sqlite3.connect('school-DBMS.db')
cur = db.cursor()

# create queries


def createTables():
    cur.execute("DROP TABLE IF EXISTS admin")
    cur.execute("DROP TABLE IF EXISTS teacher")
    cur.execute("DROP TABLE IF EXISTS student")
    cur.execute("""
     CREATE TABLE admin(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(2),
        username VARCHAR(16),
        password VARCHAR(16)
    );
    """)
    cur.execute("""
    INSERT INTO admin(name, username, password)
    VALUES('admin','admin', 'admin');
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
    cur.execute("""
    CREATE TABLE teacher(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name VARCHAR(16),
        last_name VARCHAR(16),
        username VARCHAR(16),
        password VARCHAR(16),
        gender VARCHAR(1),
        date_of_birth DATE,
        security_question VARCHAR(30),
        security_answer VARCHAR(30)
    );
    """)
    cur.execute("""
    CREATE TABLE student_teacher(
        student_id INTEGER,
        teacher_id INTEGER,
        mark INTEGER,
        date DATE,
        PRIMARY KEY(student_id, teacher_id),
        FOREIGN KEY(student_id) REFERENCES student(id)
        ON DELETE CASCADE,
        FOREIGN KEY(teacher_id) REFERENCES teacher(id)
        ON DELETE CASCADE
    );

    """)
    res = cur.execute("""
    SELECT * FROM student
    """)
    db.commit()

    for resor in res:
        print(resor)
    print('success')
    db.close()


if __name__ == "__main__":
    createTables()
