from django.urls import path

from.views import json_msg

urlpatterns = [
    path("", json_msg, name="home"),
]