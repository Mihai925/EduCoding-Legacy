__author__ = 'varun'

STUDENT_GROUP_NAME = "Student"
TEACHER_GROUP_NAME = "Teacher"


def is_student(user):
    return user.groups.filter(name=STUDENT_GROUP_NAME).count() == 1


def is_teacher(user):
    return user.groups.filter(name=TEACHER_GROUP_NAME).count() == 1