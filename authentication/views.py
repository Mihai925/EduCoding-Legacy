import logging

from django.contrib.auth import REDIRECT_FIELD_NAME, login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect

from authentication.models import Invitation

LOGGER = logging.getLogger(__name__)


# TODO: Pass the success_url to a new controller to delete the invitation
@method_decorator(user_passes_test(lambda u: not u.is_authenticated(), redirect_field_name='/'), name='dispatch')
class TeacherRegistration(CreateView):
    template_name = 'authentication/teacher_registration.html'
    success_url = '/postreg/'
    model = User
    fields = ['username', 'password', 'first_name', 'last_name']

    def get(self, request, *args, **kwargs):
        if 'invitation_code' not in request.GET:
            return HttpResponseRedirect('/')

        invitation_code = request.GET['invitation_code']
        try:
            Invitation.objects.get(invitation_code=invitation_code)
        except ObjectDoesNotExist:
            return HttpResponseRedirect('/')
        return super(TeacherRegistration, self).get(request)

    def get_success_url(self):

        Group.objects.get_or_create(name='Teacher')[0].user_set.add(self.object)
        return super(TeacherRegistration, self).get_success_url()

    def form_valid(self, form):
        print self.request.POST['invitation_code']
        form.instance.email = form.instance.username
        return super(TeacherRegistration, self).form_valid(form)


class LoginView(FormView):
    """
    Provides the ability to login (with username/email and password)
    """

    success_url = '/success/'
    form_class = AuthenticationForm
    redirect_field_name = REDIRECT_FIELD_NAME

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        # Setting a test cookie, to make sure the user has cookies enabled
        request.session.set_test_cookie()

        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def get(self):
        return redirect('/')

    def form_valid(self, form):
        print "Getting user"
        user = authenticate(username=self.request.POST['username'], password=self.request.POST['password'])
        print user
        if user is None:
            return redirect('/')
        login(self.request, form.get_user())

        if self.request.session.test_cookie_worked():
            self.request.session.delete_test_cookie()
        return super(LoginView, self).form_valid(form)

    def form_invalid(self, form):
        return redirect('/')

    def get_success_url(self):
        return self.success_url
