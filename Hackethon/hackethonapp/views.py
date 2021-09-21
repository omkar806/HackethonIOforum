from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
import pyrebase 
# Create your views here.


def index (requests):
    return HttpResponse("This is my webpage")