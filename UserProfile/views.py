from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import get_template
from django.core.context_processors import csrf
from .forms import UserProfileForm


@login_required
def settings_page(request):
    profile_form = UserProfileForm(initial={'first_name': request.user.first_name,
                                            'last_name': request.user.last_name,
                                            'email': request.user.email})
    context = RequestContext(request, {
        'name': request.user.first_name,
        'profile': profile_form
    })
    context.update(csrf(request))
    return HttpResponse(get_template('UserProfile/TeacherProfile.html').render(context))


@login_required
def update_user_profile(request):
    profile_form = UserProfileForm(request.POST)
    if profile_form.is_valid():
        first_name = profile_form.cleaned_data["first_name"]
        last_name = profile_form.cleaned_data["last_name"]
        email = profile_form.cleaned_data["email"]
        password = profile_form.cleaned_data["old_password"]
        new_password = profile_form.cleaned_data["new_password"]
        repeat_new_password = profile_form.cleaned_data["repeat_new_password"]
        request.user.first_name = first_name
        request.user.last_name = last_name
        request.user.email = email
        #if check_username_password_is_valid(username=request.user.username,
        #                                    password=password) and new_password is repeat_new_password:
        #    request.user.set_password(new_password)
        request.user.save()
    return HttpResponseRedirect("/Profile/")