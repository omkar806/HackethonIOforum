from django.contrib import admin
from django.urls import path,include
from hackethonapp import views
urlpatterns = [
    path("" , views.index , name="index"),
    path("signup/" , views.signup , name="signup")
    # path("postsignup" , views.postsignup , name="postsignup")
]
