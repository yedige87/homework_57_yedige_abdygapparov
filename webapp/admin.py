from django.contrib import admin
from webapp.models import ToDo

# Register your models here.
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date_todo', 'state')
    list_filter = ('id', 'title', 'date_todo', 'state')
    search_fields = ('title', 'date_todo')
    fields = ('description', 'title', 'date_todo', 'state')


admin.site.register(ToDo, ToDoAdmin)
