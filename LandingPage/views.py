from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import get_template
from authentication.forms import LoginForm

from .forms import ContactUsForm
from .queries import get_landing_page_data
from Utils.Email import Email
from codeaton.settings import HELLO_EMAIL

import logging

LOGGER = logging.getLogger(__name__)


def home_page(request):
    context = RequestContext(request,
                      {'login_form': LoginForm(),
                       'landing_page': get_landing_page_data(),
                       'contact_us': ContactUsForm()})
    try:
        error_text = request.session["error"]
        request.session["error"] = None
        context.update({"error_text": error_text})
    except KeyError:
        pass
    return HttpResponse(get_template("LandingPage/home_page.html").render(context))


def contact_us_form(request):
    contact_us = ContactUsForm(request.POST)
    if contact_us.is_valid():
        name = contact_us.cleaned_data["name"]
        email = contact_us.cleaned_data["email"]
        phone = contact_us.cleaned_data["phone"]
        message = contact_us.cleaned_data["message"]
        context = RequestContext(request,
        {
            'name': name,
            'email': email,
            'phone': phone,
            'message': message
        })
        email_text = get_template("LandingPage/contact_us_email.html").render(context)
        email = Email(to_address=HELLO_EMAIL, message=email_text, subject="Contact Us Form")
        LOGGER.info("Sending Contact Us email submission success: " + str(email.send()))
    return HttpResponseRedirect("/")
