from django.conf.urls import url

from .views import PanelView

urlpatterns = [
    url(r'^panel/\Z', PanelView.as_view())
]