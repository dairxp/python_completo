from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import render, redirect
from .forms import CreateNewTask 
# Create your views here.
def index(request):
    title_inicio = 'Django Course!!'
    return render(request, 'index.html', {
        'title': title_inicio
    })   

def hello(request, id):
    print(id+100*2)
    return HttpResponse("<h1> Hello  %s</h1>" %id)

def about(request):
    username_dev= 'DairXP'
    return render(request, 'about.html', {
        'username': username_dev
    })

def projects(request):
    #projects= list(Project.objects.values())
    projects= Project.objects.all()
    return render(request, 'projects.html', {
        'projects_temp':projects
    })

def tasks(request):
    #task=Task.objects.get(id=id)
    tasks =Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks': tasks
    })

def create_task(request):
    if request.method == 'GET':
        #show inteface
        return render(request, 'create_task.html', {
        'form': CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'],description=request.POST['description'], project_id=1)
        return redirect('/tasks/')
    