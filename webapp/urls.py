from django.urls import path

from webapp.views.todos import add_view, edit_view, todo_view, delete_view
from webapp.views.base import index_view

urlpatterns = [
    path("", index_view, name='index'),
    path('add', add_view, name='todo_add'),
    path('edit/<int:pk>', edit_view, name='todo_edit'),
    path('todo/<int:pk>', todo_view, name='todo_view'),
    path('delete/<int:pk>', delete_view, name='todo_delete'),
]