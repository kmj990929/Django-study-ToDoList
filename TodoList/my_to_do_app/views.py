from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from django.urls import reverse

# Create your views here.

def createTodo(request):
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content = user_input_str)
    new_todo.save()
    return HttpResponseRedirect(reverse('index'))
    #return HttpResponse("create Todo =>" + user_input_str)

def index(request):
    todos = Todo.objects.all()
    content = {'todos':todos}
    return render(request, 'bell_app/index.html',content)

def deleteTodo(request):
    delete_todo_id = request.GET['todoNum']
    print("완료한 todo의 id",delete_todo_id)
    todo = Todo.objects.get(id = delete_todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('index'))