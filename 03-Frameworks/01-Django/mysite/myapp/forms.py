from django import forms

class CreateNewTask(forms.Form):
    title=forms.CharField(label="Titulo de tarea", max_length=200)
    description=forms.CharField(label= "description de la tarea",widget=forms.Textarea)

class CreateNewProjects(forms.Form):
    name=forms.CharField(label= "Nombre del proyeto: ", max_length=200) 
    