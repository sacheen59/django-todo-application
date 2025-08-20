from django.shortcuts import render,redirect
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

def delete(request,id):
    todo = Task.objects.get(id = id)
    todo.delete()
    # return redirect("/todo/index/")
    return redirect("index-page")

