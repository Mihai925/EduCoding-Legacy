from django.http import HttpResponse, HttpResponseServerError, HttpResponseBadRequest
from .class_queries import get_class_by_teacher, get_students_by_class_id, remove_student_by_class_id_and_username, \
    add_new_class, delete_class as remove_class, get_invitations_for_class
from .Invitations import send_invites, send_invitation_email, delete_invitation as delete_invitation_model
from .forms import AddStudentForm
from authentication.authenticate import group_required
from django.contrib.auth.decorators import login_required
from Utils.UserGroups import TEACHER as TEACHER_GROUP
from django.views.generic import TemplateView
from django.shortcuts import render
from django.utils.decorators import method_decorator


class ClassManagementHomeView(TemplateView):
    template_name = "class_management/class_management_page.html"
    template_pars = {
        'add_student': AddStudentForm()
    }

    @method_decorator(login_required)
    @method_decorator(group_required(TEACHER_GROUP))
    def get(self, request, *args, **kwargs):
        classes = get_class_by_teacher(request.user);
        self.template_pars['classes'] = classes
        return render(request, self.template_name, self.template_pars)


class ClassStudentsView(TemplateView):
    template_name = "class_management/students_for_class.html"

    @method_decorator(login_required)
    @method_decorator(group_required(TEACHER_GROUP))
    def get(self, request, *args, **kwargs):
        class_id = request.GET["class_id"]
        template_pars = {
            'course_id': class_id,
            'students': self.__get_students_in_class(class_id),
            'invitations': self.__get_invitations_for_class(class_id)
        }
        return render(request, self.template_name, template_pars)

    @staticmethod
    def __get_invitations_for_class(class_id):
        return get_invitations_for_class(class_id)

    @staticmethod
    def __get_students_in_class(class_id):
        students = get_students_by_class_id(class_id)
        result = []
        for first_name, last_name, u_id in students:
            result.append((first_name + " " + last_name, u_id))
        return result


# The following views are used by Ajax, they will remain function-based for now:
@login_required
@group_required(TEACHER_GROUP)
def remove_student_from_class(request):
    class_id = request.GET["class_id"]
    username = request.GET["username"]
    if remove_student_by_class_id_and_username(class_id, username):
        return HttpResponse("removed")
    return HttpResponseBadRequest("Error occurred while removing student from class")


@login_required
@group_required(TEACHER_GROUP)
def send_invites_to_students(request):
    try:
        invites = eval(request.GET["invites"])
        class_id = eval(request.GET["class_id"])
        if send_invites(invites, request.user, class_id):
            return HttpResponse("")
    except Exception as e:
        return HttpResponseBadRequest(e.message)


@login_required
@group_required(TEACHER_GROUP)
def create_new_class(request):
    class_name = request.POST['class_name']
    class_description = request.POST['class_description']
    add_new_class(class_name, class_description, request.user)
    return HttpResponse("success")


@login_required
@group_required(TEACHER_GROUP)
def delete_class(request):
    class_id = request.POST["class_id"]
    if remove_class(class_id):
        return HttpResponse("")
    else:
        return HttpResponseServerError("Invalid Class")


@login_required
@group_required(TEACHER_GROUP)
def resend_invitation(request, invitation_id):
    if send_invitation_email(invitation_id, request.user):
        return HttpResponse("")
    return HttpResponseServerError("Not authenticated for this. Please login first.")


@login_required
@group_required(TEACHER_GROUP)
def delete_invitation(request, invitation_id):
    if delete_invitation_model(invitation_id, request.user):
        return HttpResponse("")
    return HttpResponseServerError("Not authenticated for this. Please login first.")
