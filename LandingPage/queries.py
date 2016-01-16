__author__ = 'varun'

from .models import LandingPage as LandingPageModel
from .LandingPageDataStructure import LandingPage, Feature


def get_landing_page_data():
    landing_page = LandingPageModel.objects.all()[0]
    features = []
    for f in landing_page.features.all():
        features.append(Feature(title=f.title, description=f.description, icon=f.icon))

    return LandingPage(description=landing_page.description, features=features[0:3])

