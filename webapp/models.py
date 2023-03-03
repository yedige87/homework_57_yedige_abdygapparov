from django.db import models


# Create your models here.
class ToDo(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Задача')
    description = models.TextField(max_length=1000, null=False, blank=False, verbose_name='Описание')
    date_todo = models.CharField(max_length=20, null=False, blank=False, verbose_name='Исполнить до')
    state = models.CharField(max_length=20, null=False, blank=False, verbose_name='Состояние')

    def __str__(self):
        return f"{self.title} - {self.state}"
