import re
from datetime import datetime


def check_date(ymd):
    pattern = "\d\d\d\d-\d\d-\d\d"
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


# while True:
#     ymd = input('Введите дату : ')
#     result = check_date(ymd)
#     print(result)
#     if result == ' Корректно!':
#         break
