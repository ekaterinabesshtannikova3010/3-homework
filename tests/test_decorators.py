from src.decorators import log
import pytest


@log(filename="mytlog.txt")
def my_function(x, y):
    return x / y


def test_correct_input():
    """Тест на успешное окончание."""
    log_file = "mytlog.txt"
    result = my_function(10, 20)
    assert result == 0.5
    with open(log_file, "r") as f:
        rdb = f.read()
        assert "my_function ok" in rdb


def test_incorrect_input():
    """Тест на некорректный ввод данных."""
    # log_file = "mytlog.txt"
    with pytest.raises(TypeError):
        result = my_function(0, 20)
        assert "TypeError: unsupported operand type(s) for /: 'str' and 'int'" in result
