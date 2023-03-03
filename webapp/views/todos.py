from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView

from webapp.forms import check_date
from webapp.models import ToDo


states = [{'id': '0', 'state': 'new', 'rus': 'Новая задача'},
          {'id': '1', 'state': 'processing', 'rus': 'В процессе выполнения'},
          {'id': '2', 'state': 'complited', 'rus': 'Задача завершена'}]


def add_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'add.html', context={'states': states})
    print(request.POST)
    errors = {}
    todo_data = {
        'title': request.POST.get('title'),
        'date_todo': request.POST.get('date_todo'),
        'state': request.POST.get('state'),
        'description': request.POST.get('description'),
    }

    if todo_data['title'] == '':
        errors['title'] = ' Это поле должно быть заполнено!'
    result = check_date(todo_data['date_todo'])
    if result != ' Корректно!':
        errors['date_todo'] = result
    if todo_data['description'] == '':
        errors['description'] = ' Это поле должно быть заполнено!'
    if errors:
        return render(request, 'add.html', context={'states': states, 'todo': todo_data, 'errors': errors})
    todo = ToDo.objects.create(**todo_data)
    return redirect(reverse('todo_view', kwargs={'pk': todo.pk}))


def edit_view(request: WSGIRequest, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    if request.method == "GET":
        return render(request, 'edit.html', context={'todo': todo, 'states': states})
    print(request.POST)
    errors = {}
    todo.title = request.POST.get('title')
    todo.date_todo = request.POST.get('date_todo')
    todo.state = request.POST.get('state')
    todo.description = request.POST.get('description')
    if todo.title == '':
        errors['title'] = ' Это поле должно быть заполнено!'
    result = check_date(todo.date_todo)
    if result != ' Корректно!':
        errors['date_todo'] = result
    if todo.description == '':
        errors['description'] = ' Это поле должно быть заполнено!'
    if errors:
        return render(request, 'edit.html', context={'todo': todo, 'states': states, 'errors': errors})
    todo.save()
    return redirect(reverse('todo_view', kwargs={'pk': todo.pk}))
    # return redirect('todo_view', pk=todo.pk)


def delete_view(request, pk):
    todo = get_object_or_404(ToDo, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'todo': todo})
    elif request.method == 'POST':
        todo.delete()
        return redirect('index')


class ToDoView(TemplateView):
    template_name = 'view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo'] = get_object_or_404(ToDo, pk=kwargs['pk'])
        return context