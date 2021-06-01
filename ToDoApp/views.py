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
        form = ToDoForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            Todo.objects.create(text=text)
        return redirect('home')
    return HttpResponse("Form not submitted.")


def delete_todo(request, todo_id):
    if request.method == 'POST':
        todo_item = Todo.objects.get(pk=todo_id)
        todo_item.delete()
        return redirect('home')
    return HttpResponse("Method not allowed!")


def edit_todo(request, todo_id):
    todo_obj = Todo.objects.get(pk=todo_id)

    form = ToDoForm(initial={'text': todo_obj.text})

    if request.method == 'POST':
        form = ToDoForm(request.POST)
        if form.is_valid():
            todo_obj.text = form.cleaned_data.get('text')
            todo_obj.save()
            return redirect('home')

    context = {"app_name": "ToDoApp", 'form': form, 'todo_obj': todo_obj}
    return render(request, 'edit.html', context)
