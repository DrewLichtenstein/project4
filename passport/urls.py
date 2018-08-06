from django.urls import path
from django.conf import settings

from . import views

urlpatterns = [
    path("signup", views.signup, name='signup'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("login_redirect",views.login_redirect,name="login_redirect"),
    path("your_passport",views.your_passport,name="your_passport"),
    path("add_park_information",views.add_park_information, name="add_park_information"),
    path("submit_review", views.submit_review, name="submit_review"),
    path("add_friend", views.add_friend, name="add_friend"),
    path("remove_from_passport", views.remove_from_passport, name="remove_from_passport"),
    path('', views.index, name='index'),
]