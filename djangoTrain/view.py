from django.http import HttpResponse
from django.shortcuts import render
def homepage(req):
    return render(req,'home.html')
def about(req):
    return render(req,'about.html')
