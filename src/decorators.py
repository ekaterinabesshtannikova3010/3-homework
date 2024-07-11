def log(filename=None):
    """
    Декоратор для логирования вызовов функции.
    Параметры:
    filename (str): Имя файла для логирования. Если не указано, лог выводится в консоль.
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a") as logfile:
                        logfile.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok\n")
            except Exception as e:
                if filename:
                    with open(filename, "a") as logfile:
                        logfile.write(f"{func.__name__} error: {type(e)}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {type(e)}. Inputs: {args}, {kwargs}\n")
                raise
            return result

        return wrapper

    return decorator
