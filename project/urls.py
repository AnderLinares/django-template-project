from django.conf.urls import url, include, static
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.app0.urls', namespace="app0")),
    url(r'^', include('apps.app1.urls', namespace="app1")),
]

if settings.DEBUG:
    urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)