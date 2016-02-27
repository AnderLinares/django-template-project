from django.conf.urls import url, include
from .views import app1View

urlpatterns = [
    url(r'^app1/$', app1View.as_view(), name="app1View"),
]