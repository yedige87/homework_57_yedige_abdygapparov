from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets


class ToDoForm(forms.Form):
    title = forms.CharField(max_length=100, required=True, null=False, blank=False, label='Задача')
    description = forms.TextField(max_length=1000, required=True, label='Описание', widget=widgets.Textarea)
    date_todo = forms.CharField(max_length=20, required=True, label='Исполнить до')

    def clean_title(self):
        title = self.cleaned_data.get('title"')
        if len(title) < 2:
            raise ValidationError('Заголовок должен быть длиннее 2 символов')
        return title
