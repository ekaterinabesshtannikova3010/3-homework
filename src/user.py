def choice_status():
    """Обработка ввода пользователя по статусу операции"""
    while True:
        user_str = input("Введите статус, по которому необходимо выполнить фильтрацию. Доступные для фильтровки "
                         "статусы: EXECUTED, CANCELED, PENDING: ").upper()
        if user_str in ["EXECUTED", "CANCELED", "PENDING"]:
            return user_str
        else:
            print(f"Статус операции '{user_str}' недоступен.")

# choice_status()