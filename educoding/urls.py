from django.conf.urls import patterns, include, url
from django.contrib import admin
from authentication import urls as auth_urls
from Class import urls as class_urls
from Exercise import urls as exercise_urls
from LandingPage import urls as landing_urls
from UserProfile import urls as profile_urls
from settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static


home_page_pattern = [url(r'^$', include(landing_urls.urlpatterns))]

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^selectable/', include('selectable.urls')),
                       url(r'^authentication/', include(auth_urls.urlpatterns)),
                       url(r'^Class/', include(class_urls.urlpatterns)),
                       url(r'^Exercise/', include(exercise_urls.urlpatterns)),
                       url(r'^Profile/', include(profile_urls.urlpatterns)),
                       url(r'^$', include(home_page_pattern))
) + static(MEDIA_URL, document_root=MEDIA_ROOT)