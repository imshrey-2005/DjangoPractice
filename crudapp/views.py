from django.shortcuts import render
from crudapp.models import Task
# Create your views here.
def index(request):
    task=Task.objects.all() 
    context={'task':task} # Fetch all tasks from the database
    return render(request,'crudapp/index.html',context)
