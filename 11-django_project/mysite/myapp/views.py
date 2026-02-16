from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'index.html')   

def hello(request, id):
    print(id+100*2)
    return HttpResponse("<h1> Hello  %s</h1>" %id)

def about(request):
    return render(request, 'about.html')

def projects(request):
    projects= list(Project.objects.values())
    return render(request, 'projects.html')

def tasks(request):
    #task=Task.objects.get(id=id)
    return render(request, 'tasks.html')
