def get_data(date_str: str) -> str:
    """Функция, возвращающая строку с датой в формате DD.MM.YYYY """
    no_format_date = datetime.strptime(date_str[:10], ("%Y-%m-%d"))
    format_date = no_format_date.strftime("%d.%m.%Y")
    return format_date

print(get_data)