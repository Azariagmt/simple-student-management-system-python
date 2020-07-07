from db import student_teacher
from datetime import date
from db import general_DB

def grade_student(teacher_id):
    student_id = int(input('Enter student id \n'))
    course = input('Enter course name \n')
    mark = int(input('Enter student grade'))
    send_dict = {
        'student_id': student_id,
        'teacher_id': teacher_id,
        'course': course,
        'mark': mark,
        'date': date.today()
    }

    student_teacher.add_grade(**send_dict)

def set_security_question(teacher_id):
    general_DB.set_security_question(teacher_id, 'teacher')


def change_password(username):
    general_DB.changePassword(username, 'teacher')
