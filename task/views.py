from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# function base views / class based views

def index(request):
    todos = [
        {
            'id': 1,
            'title': 'Buy groceries',
            'description': 'Milk, Bread, Eggs'
        },
        {
            'id': 2,
            'title': 'Go to gym',
            'description': 'Chest, Back, Legs'
        },
        {
            'id': 3,
            'title': 'Read a book',
            'description': 'The Catcher in the Rye'
        },
        {
            'id': 4,
            'title': 'Watch a movie',
            'description': 'Inception'
        },
        {
            'id': 5,
            'title': 'Play football',
            'description': 'With friends'
        },
        {
            'id': 6,
            'title': 'Go to the beach',
            'description': 'With family'
        }
    ]
    
    context = {
        "todos": todos
    }
    return render(request,'task/index.html',context=context)

def detail_page(request,task_id):
    return HttpResponse(task_id)