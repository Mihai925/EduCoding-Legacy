import logging

from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User, Group
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect

from authentication.models import Invitation
LOGGER = logging.getLogger(__name__)

#TODO: Pass the success_url to a new controller to delete the invitation
@method_decorator(user_passes_test(lambda u: not u.is_authenticated(), redirect_field_name='/'), name='dispatch')
class TeacherRegistration(CreateView):
    template_name = 'authentication/teacher_registration.html'
    success_url = '/'
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
        form.instance.email = form.instance.username
        return super(TeacherRegistration, self).form_valid(form)
