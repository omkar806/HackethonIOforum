from django.contrib import admin
from django.urls import path,include
from hackethonapp import views
urlpatterns = [
    path("" , views.index , name="index"),
    
]
