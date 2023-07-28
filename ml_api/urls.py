from django.urls import path, include
from .views import create_user,login,test

urlpatterns = [
    path("create_user/",create_user),
    path("login/",login),
    path("test/",test)
]