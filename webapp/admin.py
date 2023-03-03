from django.contrib import admin
from webapp.models import ToDo


# Register your models here.
class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'deadline', 'status', 'type')
    list_filter = ('id', 'title', 'deadline', 'status', 'type')
    search_fields = ('title', 'deadline', 'type')
    fields = ('description', 'title', 'deadline', 'status', 'type')


admin.site.register(ToDo, ToDoAdmin)
