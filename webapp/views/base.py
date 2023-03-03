from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, redirect

from webapp.models import ToDo

actions = [{'id': '0', 'action': 'выберите действие'}, {'id': '1', 'action': 'добавить задачу'},
           {'id': '2', 'action': 'удалить с подтверждением'}, {'id': '3', 'action': 'редактировать задачу'},
           {'id': '4', 'action': 'показать задачу'}]


def index_view(request: WSGIRequest):
    if request.method == "GET":
        print(request.GET)
        todos = ToDo.objects.all().order_by('id')
        context = {'todos': todos, 'actions': actions}
        return render(request, 'index.html', context=context)
    print(request.POST)
    del_button = request.POST.get('delete_button')
    check_del = request.POST.getlist('check_del')
    # list_del = json.loads(check_del)

    print('check_del =', check_del, type(check_del))
    if del_button:
        if check_del:
            for ind in check_del:
                todo = ToDo.objects.get(pk=ind)
                print('ind = ', ind)
                todo.delete()
    else:
        action = request.POST.get('action')
        task = request.POST.get('task')
        action = int(action)
        print("action - ", action)

        if not task:
            task = '0'
        task = int(task)
        print("task - ", task)

        if action == 1:
            return render(request, 'add.html')
        if action != 0 and task != 0:
            todo = get_object_or_404(ToDo, pk=task)
            if action == 2 and task != 0:
                return redirect('todo_delete', pk=todo.id)
            elif action == 3 and task != 0:
                return redirect('todo_edit', pk=todo.id)
            elif action == 4 and task != 0:
                return redirect('todo_view', pk=todo.id)

    todos = ToDo.objects.all().order_by('id')
    return render(request, 'index.html', context={'todos': todos, 'actions': actions})
