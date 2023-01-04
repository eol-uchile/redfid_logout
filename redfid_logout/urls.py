from django.contrib import admin
from django.conf.urls import url
from .views import *


urlpatterns = [
    url('logout_get/', RedfidLogoutGet.as_view(), name='logout_get'),
    url('logout_post/', RedfidLogoutPost.as_view(), name='logout_post'),
]
