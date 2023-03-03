from django.urls import path

from webapp.views.todos import ToDoAddView, ToDoEditView, ToDoView, delete_view
from webapp.views.base import index_view

urlpatterns = [
    path("", index_view, name='index'),
    path('add', ToDoAddView.as_view(), name='todo_add'),
    path('edit/<int:pk>', ToDoEditView.as_view(), name='todo_edit'),
    path('todo/<int:pk>', ToDoView.as_view(), name='todo_view'),
    path('delete/<int:pk>', delete_view, name='todo_delete'),
]
