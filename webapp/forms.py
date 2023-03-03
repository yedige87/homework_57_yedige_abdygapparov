import re
from datetime import datetime

from django import forms
from django.core.exceptions import ValidationError

from webapp.models import ToDo


def check_date(ymd):
    pattern = '\d\d\d\d-\d\d-\d\d'
    result = ' Ошибки: '
    if re.fullmatch(pattern, ymd):
        year = int(ymd[0:4])
        month = int(ymd[5:7])
        day = int(ymd[8:10])
        print(year, month, day)
        if year < 2000 or year > 2100:
            result += 'Год за пределами столетия. '
        if month < 1 or month > 12:
            result += 'Месяц за пределами 1-12. '
        if day < 1 or day > 31:
            result += 'День за пределами 1-31. '

        if result == ' Ошибки: ':
            try:
                new_date = datetime.strptime(ymd, "%Y-%m-%d")
            except ValueError:
                result += 'Введите корректный день для данного месяца !'
            else:
                print(new_date)
                result = ' Корректно!'

    else:
        result += 'Введите дату в формате ГГГГ-ММ-ДД !'
    return result


class ToDoForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ('title', 'description', 'deadline', 'status', 'positions', 'type')
        labels = {
            'title': 'Задача',
            'description': 'Описание',
            'deadline': 'Дедлайн',
            'status': 'Статус',
            'positions': 'Должность',
            'type': 'Тип'
        }

    def clean_deadline(self):
        deadline = self.cleaned_data.get('deadline')
        result = check_date(deadline)
        if result != ' Корректно!':
            raise ValidationError(result)
        return deadline
