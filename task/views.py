from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# Create your views here.
# function base views / class based views

def index(request):
    todos = Task.objects.all()
    context = {
        "todos": todos
    }
    return render(request,'task/index.html',context=context)

