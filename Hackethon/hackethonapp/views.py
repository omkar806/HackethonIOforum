from django.http.response import HttpResponse
from django.shortcuts import render,HttpResponse
import pyrebase 
# Create your views here.


def index (request):
    return render (request ,"index.html")

