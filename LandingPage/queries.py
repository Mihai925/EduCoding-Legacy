__author__ = 'varun'

from .models import LandingPage as LandingPageModel
from .LandingPageDataStructure import LandingPage, Feature


def get_landing_page_data():
    return LandingPageModel.objects.all()[0]


