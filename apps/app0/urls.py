from django.conf.urls import url, include
from .views import app0View

urlpatterns = [
    url(r'^$', app0View.as_view(), name="app0Wiew"),
]