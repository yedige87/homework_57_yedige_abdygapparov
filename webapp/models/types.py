from django.db import models


class Type(models.Model):
    type = models.CharField(
        max_length=20,
        verbose_name='Тип'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата и время создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата и время изменения'
    )

    def __str__(self):
        return self.type
