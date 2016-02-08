import logging

from django.http import HttpResponse, HttpResponseRedirect, HttpResponseBadRequest
from django.template import Context
from django.template.loader import get_template
from django.core.context_processors import csrf

from .forms import LoginForm, RegisterForm
from .authenticate import login_user, logout_user, does_username_exist, register_student as register_student_in_db, \
    does_user_with_email_exist
from .subscription import add_subscriber
from Utils.user_utils import is_student, is_teacher



LOGGER = logging.getLogger(__name__)


def login(request):
    login_form = LoginForm(request.POST)
    if login_form.is_valid():
        username = login_form.cleaned_data["username"]
        password = login_form.cleaned_data["password"]
        if login_user(username, password, request):
            if is_student(request.user):
                return HttpResponseRedirect("/Exercise/student")
            elif is_teacher(request.user):
                return HttpResponseRedirect("/Class/")
            pass
        else:
            request.session["error"] = "Invalid Username/Password"
        return HttpResponseRedirect("/")
    return HttpResponseRedirect("/")


def logout(request):
    logout_user(request)
    return HttpResponseRedirect("/")


def authentication_page(request):
    context = Context({'login_form': LoginForm()})
    try:
        error_text = request.session["error"]
        request.session["error"] = None
        context.update({"error_text": error_text})
    except KeyError:
        pass
    context.update(csrf(request))
    return HttpResponse(get_template("authentication/login_page.html").render(context))


def check_username(request):
    if request.is_ajax():
        username = request.POST["username"]
        if does_username_exist(username):
            return HttpResponse("yes")
        else:
            return HttpResponse("no")
    return HttpResponseBadRequest("Invalid Query")


def check_email(request):
    if request.is_ajax():
        email = request.POST["email"]
        if does_user_with_email_exist(email):
            return HttpResponse("yes")
        else:
            return HttpResponse("no")
    return HttpResponseBadRequest("Invalid Query")


def register_student_page(request, invitation_code, errors={}, form=None):
    if invitation_code is not None:
        try:
            invitation = Invitation(invitation_code=invitation_code)
            if form is None:
                form = RegisterForm(initial={'email': invitation.email})
            context = Context({
                'register_form': form,
                'is_not_validated': False,
                'teacher_name': invitation.teacher.first_name + " " + invitation.teacher.last_name
            })
            context.update(errors)
            request.session["invitation_code"] = invitation.invitation_code
            context.update(csrf(request))
            return HttpResponse(get_template("authentication/register_page.html").render(context))
        except Exception as e:
            LOGGER.error(e)
            return HttpResponse(
                get_template("authentication/register_page.html").render(Context({'is_not_validated': True})))
    return HttpResponseRedirect("/")


def register_student(request):
    register_form = RegisterForm(request.POST)
    if register_form.is_valid():
        register_form.clean()
        try:
            invitation_code = request.session["invitation_code"]

            username = register_form.cleaned_data["username"]
            password = register_form.cleaned_data["password"]
            first_name = register_form.cleaned_data["firstName"]
            last_name = register_form.cleaned_data["lastName"]
            email = register_form.cleaned_data["email"]
            if does_username_exist(username=username):
                return register_student_page(request=request, invitation_code=request.session["invitation_code"],
                                             errors={"username_error": "Username already taken."}, form=register_form)
            elif does_user_with_email_exist(email=email):
                return register_student_page(request=request, invitation_code=request.session["invitation_code"],
                                             errors={"email_error": "An account with this email already exists."},
                                             form=register_form)
            register_student_in_db(username, password, email, first_name, last_name)

            request.session["invitation_code"] = ""

        except KeyError as e:
            LOGGER.error(e)
        except Exception as e:
            LOGGER.error(e)
    return register_student_page(request=request, invitation_code=request.session["invitation_code"])


def automatic_login_teacher(request):
    login_user(username="varun", password="varun9193", request=request)
    return HttpResponseRedirect("/Class/")


def automatic_login_student(request):
    login_user(username="stud1", password="abcd", request=request)
    return HttpResponseRedirect("/Exercise/student")


def subscribe_user(request):
    email = request.POST["email"]
    try:
        add_subscriber(email)
        return HttpResponse("done")
    except:
        return HttpResponse("error")

