from datetime import datetime

def get_data(date: str) -> str:
    """Функция преобразующая дату формат даты"""
    date_it = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S:%f")
    formated_date = date_it.strptime("%d.%m.%Y")
    return formated_date

print(get_data(2018-07-11T02:26:18.671407))