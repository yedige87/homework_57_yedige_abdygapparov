from django.db import models
from django.db.models import TextChoices


class StatusChoice(TextChoices):
    NEW = 'new', 'Новая'
    IN_PROGRESS = 'in_progress', 'Выполняется'
    DONE = 'done', 'Завершена'


class ToDo(models.Model):
    status = models.CharField(choices=StatusChoice.choices, default=StatusChoice.NEW, verbose_name='Статус',
                              max_length=20)
    title = models.CharField(max_length=100, null=False, blank=False, verbose_name='Задача')
    description = models.TextField(max_length=1000, null=False, blank=False, verbose_name='Описание')
    deadline = models.CharField(max_length=20, null=False, blank=False, verbose_name='Исполнить до')
    positions = models.ManyToManyField(to='webapp.Position', related_name='todos', blank=True)
    type = models.ForeignKey(
        verbose_name='Type',
        to='webapp.Type',
        null=True,
        blank=False,
        related_name='todo',
        on_delete=models.RESTRICT
    )

    class Meta:
        verbose_name = 'Задачи'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return f"{self.title} - {self.status}"
