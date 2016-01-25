from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import RedirectView
from authentication import urls as auth_urls
from Class import urls as class_urls
from Exercise import urls as exercise_urls
from LandingPage import urls as landing_urls
from .settings import USE_LANDING_PAGE
from UserProfile import urls as profile_urls


home_page_pattern = []
if USE_LANDING_PAGE:
    home_page_pattern.append(url(r'^$', include(landing_urls.urlpatterns)))
else:
    home_page_pattern.append(url(r'^$', RedirectView.as_view(url='/authentication/')))

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^selectable/', include('selectable.urls')),
                       url(r'^authentication/', include(auth_urls.urlpatterns)),
                       url(r'^Class/', include(class_urls.urlpatterns)),
                       url(r'^Exercise/', include(exercise_urls.urlpatterns)),
                       url(r'^Profile/', include(profile_urls.urlpatterns)),
                       url(r'^$', include(home_page_pattern))
)