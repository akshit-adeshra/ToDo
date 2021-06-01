from django.shortcuts import render, redirect
from django.http import HttpResponse
from ToDoApp.models import Todo
from ToDoApp.forms import ToDoForm


def home(request):
    todo_list = Todo.objects.all()
    form = ToDoForm()
    context = {"app_name": "ToDoApp", "todo_list": todo_list, 'form': form}
    return render(request, 'home.html', context)


def add_todo(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        Todo.objects.create(text=text)
        return redirect('home')
    return HttpResponse("Form not submitted.")