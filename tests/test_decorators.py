def log(filename=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, 'a') as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")
                return result
            except Exception as e:
                error_msg = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, 'a') as file:
                        file.write(error_msg + '\n')
                else:
                    print(error_msg)
                raise
        return wrapper
    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


def test_my_function(capsys):
    """
    Тест для генератора.
    """
    with capsys.disabled():
        result = my_function(1, 2)
        captured = capsys.readouterr()
        assert result == 3
        assert captured.out == ''
        assert captured.err == ''
