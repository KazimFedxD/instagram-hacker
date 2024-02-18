from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("reel/<string>/", views.reel, name="post"),
    path("login/", views.login, name="login"),
    path("login/r/<string>/", views.loginreel, name="loginreel"),
    path("login/p/<string>/", views.loginpost, name="loginpost"),
    path("p/<string>/", views.post, name="post"),
    ]

