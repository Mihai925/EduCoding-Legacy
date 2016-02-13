from django.template import RequestContext
from authentication.forms import LoginForm
from .models import Quotes
from .forms import ContactUsForm
from .queries import get_landing_page_data
from django.views.generic import View
from django.shortcuts import render

import logging

LOGGER = logging.getLogger(__name__)


class HomePageView(View):
    template_name = "LandingPage/home_page.html"
    template_pars = {
        'login_form': LoginForm(),
        'contact_us': ContactUsForm()
    }

    def get(self, request):
        self.template_pars['landing_page'] = get_landing_page_data()
        self.template_pars['quote'] = Quotes.objects.order_by('?').first()
        return render(request, self.template_name, self.template_pars)

    def post(self, request):
        form = ContactUsForm(request.POST)
        self.template_pars['landing_page'] = get_landing_page_data()
        self.template_pars['quote'] = Quotes.objects.order_by('?').first()
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            message = form.cleaned_data["message"]
            context = RequestContext(request,
                                     {
                                         'name': name,
                                         'email': email,
                                         'phone': phone,
                                         'message': message
                                     })
            print 'Success'
            # Skipping e-mail sending for now
        return render(request, self.template_name, self.template_pars)
