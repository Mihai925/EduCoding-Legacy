from django.conf.urls import url

from .views import PanelView

urlpatterns = [
    url(r'^panel/', PanelView.as_view())
]