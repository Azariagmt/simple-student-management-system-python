from student import student_home
from student import student_login
import sqlite3

# create database and connect

db = sqlite3.connect('school-DBMS.db')
cur = db.cursor()

# create queries


def createTables():
    cur.execute("DROP TABLE IF EXISTS school")
    cur.execute("DROP TABLE IF EXISTS admin")
    cur.execute("DROP TABLE IF EXISTS teacher")
    cur.execute("DROP TABLE IF EXISTS student")
    cur.execute("""
    CREATE TABLE school(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(40)
    );
    """)
    cur.execute("""
     CREATE TABLE admin(
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
    print('success')


if __name__ == "__main__":
    createTables()
