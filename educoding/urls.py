from django.conf.urls import include, url
from django.contrib import admin
from Panel import urls as panel_urls
from Class import urls as class_urls
from Exercise import urls as exercise_urls
from LandingPage import urls as landing_urls
from UserProfile import urls as profile_urls
from authentication import urls as auth_urls
from settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static


home_page_pattern = [url(r'^\Z', include(landing_urls.urlpatterns))]

urlpatterns = [

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^selectable/', include('selectable.urls')),
                       url(r'^authentication/', include(auth_urls.urlpatterns)),
                       url(r'^Class/', include(class_urls.urlpatterns)),
                       url(r'^Exercise/', include(exercise_urls.urlpatterns)),
                       url(r'^Profile/', include(profile_urls.urlpatterns)),
                       url(r'', include(panel_urls.urlpatterns)),
                       url(r'^', include(auth_urls)),
                       url(r'^\Z', include(home_page_pattern)),
                       url(r'^api/', include(exercise_urls.router.urls)),
                       url(r'^api/', include(class_urls.router.urls))
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
