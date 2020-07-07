import sqlite3
from teacher import teacher_home

db = sqlite3.connect('school-DBMS.db')
cur = db.cursor()


def add_grade(**kwargs):
    cur.execute(f"""
        INSERT INTO student_teacher('student_id', 'teacher_id', 'course', 'mark','date')
        VALUES(
        '{kwargs['student_id']}',
        '{kwargs['teacher_id']}',
        '{kwargs['course']}',
        '{kwargs['mark']}',
        '{kwargs['date']}');
        """)
    print('success inserting..')
    db.commit()
    teacher_home.teacher_home(kwargs['teacher_id'])
