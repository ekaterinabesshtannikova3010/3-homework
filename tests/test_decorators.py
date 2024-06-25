from src.decorators import log


def test_log(capsys):
    """
    Тестовая функция для декоратора log.
    """
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x + y

    my_function(1, 2)

    captured = capsys.readouterr()
    assert captured.out == ""
    assert captured.err == ""

    with open("mylog.txt", "r") as f:
        log_contents = f.read()
        assert "my_function ok\n" in log_contents
