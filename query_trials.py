import sqlite3

db = sqlite3.connect('school-DBMS.db')
cur = db.cursor()

result = cur.execute("""
SELECT * FROM student_teacher;
""")
for row in result:
    print(row)
