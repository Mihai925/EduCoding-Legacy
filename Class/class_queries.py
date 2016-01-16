from .models import Class, Invitation
from django.contrib.auth.models import User


# Given a Teacher object (User), class name and class id
def get_class_by_teacher(teacher):
    classes = Class.objects.filter(teacher=teacher)
    return [(class_i.name, class_i.description, class_i.cls_id) for class_i in classes]


# Given a class id, return a list of all the students in the class
def get_students_by_class_id(cls_id):
    a_class = Class.objects.get(cls_id=cls_id)
    return [(student.first_name, student.last_name, student.username) for student in a_class.students.all()]


def delete_class(cls_id):
    a_class = Class.objects.get(cls_id=cls_id)
    if a_class is not None:
        a_class.delete()
        return True
    return False


def add_student_to_class(cls_id, student):
    Class.objects.get(cls_id=cls_id).students.add(student)


def remove_student_from_class(cls_id, student):
    a_class = Class.objects.get(cls_id=cls_id)
    a_class.students.remove(student)
    return True


# Given class_id, and username, remove that user from the class
def remove_student_by_class_id_and_username(class_id, username):
    user = User.objects.get(username=username)
    return remove_student_from_class(class_id, user)


def add_new_class(class_name, class_description, teacher):
    new_class = Class()
    new_class.name = class_name
    new_class.description = class_description
    new_class.save()
    new_class.teacher.add(teacher)
    new_class.save()


def get_invitations_for_class(class_id):
    invites = Invitation.objects.filter(class_to_add=Class.objects.get(cls_id=class_id))
    response = []
    for inv in invites:
        response.append((inv.student_email, inv.invitation_id))
    return response
