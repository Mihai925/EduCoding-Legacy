__author__ = 'varun'

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import user_passes_test


def check_username_password_is_valid(username, password):
    if authenticate(username=username, password=password):
        return True
    return False


def login_user(username, password, request):
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request=request, user=user)
            return True
        else:
            # Account is disabled
            pass
    return False


def register_teacher(username, password, email, first_name, last_name):
    __register_user(username, password, email, first_name, last_name, "Teacher")


def __register_user(username, password, email, first_name, last_name, group_name):
    user = User.objects.create_user(username=username, password=password, email=email)
    user.first_name = first_name
    user.last_name = last_name
    g = Group.objects.get(name=group_name)
    g.user_set.add(user)
    user.save()


def register_student(username, password, email, first_name, last_name):
    __register_user(username, password, email, first_name, last_name, "Student")


def logout_user(request):
    logout(request=request)


def remove_user(username):
    user = User.objects.get(username=username)
    user.delete()


def does_username_exist(username):
    if User.objects.filter(username=username).count():
        return True
    return False


def does_user_with_email_exist(email):
    if User.objects.filter(email=email).count():
        return True
    return False


def group_required(*group_names):
    """Requires user membership in at least one of the groups passed in."""

    def in_groups(u):
        if u.is_authenticated():
            if u.is_superuser | bool(u.groups.filter(name__in=group_names)):
                return True
        return False

    return user_passes_test(in_groups)