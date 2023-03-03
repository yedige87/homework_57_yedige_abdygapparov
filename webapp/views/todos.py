from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView

from webapp.forms import ToDoForm
from webapp.models import ToDo, todo

states = [{'id': '0', 'state': 'new', 'rus': 'Новая задача'},
          {'id': '1', 'state': 'processing', 'rus': 'В процессе выполнения'},
          {'id': '2', 'state': 'complited', 'rus': 'Задача завершена'}]


class ToDoAddView(TemplateView):
    template_name = 'add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ToDoForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo_view', pk=todo.pk)
        return render(request, 'add.html', context={'form': form})


class ToDoEditView(TemplateView):
    template_name = 'edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['todo'] = get_object_or_404(ToDo, pk=kwargs['pk'])
        context['form'] = ToDoForm(instance=context['todo'])
        return context

    def post(self, request, *args, **kwargs):
        todo = get_object_or_404(ToDo, pk=kwargs['pk'])
        form = ToDoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todo_view', pk=todo.pk)
        return render(request, 'edit.html', context={'form': form, 'todo': todo})
    

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
