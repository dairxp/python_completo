from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Index page")

def hello(request, id):
    print(id+100*2)
    return HttpResponse("<h1> Hello  %s</h1>" %id)

def about(request):
    return HttpResponse("about")