def log(filename="mylog.txt"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            try:
                file = open(filename, "a")
                file.write(f"{func.__name__} ok\n")
                file.close()
            except Exception as e:
                file = open(filename, "a")
                file.write(f"{func.__name__} error: {type(e)}. Inputs: {args}, {kwargs}\n")
                file.close()
                raise
            return result
        return wrapper
    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


my_function(1, 2)
