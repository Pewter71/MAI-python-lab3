"""
Тесты проверки функций вычисления числа Фибоначчи
"""
from src.fibo import fibo_not_recursive, fibo_recursive


def test_fibo_not_recursive_zero():
    """Тест числа Фибоначчи для нуля нерекурсивно"""
    assert fibo_not_recursive(0) == 0


def test_fibo_not_recursive_one():
    """Тест числа Фибоначчи для единицы нерекурсивно"""
    assert fibo_not_recursive(1) == 1


def test_fibo_not_recursive_five():
    """Тест числа Фибоначчи для пяти нерекурсивно"""
    assert fibo_not_recursive(5) == 5


def test_fibo_not_recursive_ten():
    """Тест числа Фибоначчи для десяти нерекурсивно"""
    assert fibo_not_recursive(10) == 55


def test_fibo_not_recursive_negative():
    """Тест числа Фибоначчи для отрицательного числа нерекурсивно"""
    assert fibo_not_recursive(-1) == -1


def test_fibo_recursive_zero():
    """Тест числа Фибоначчи для нуля рекурсивно"""
    assert fibo_recursive(0) == 0


def test_fibo_recursive_one():
    """Тест числа Фибоначчи для единицы рекурсивно"""
    assert fibo_recursive(1) == 1


def test_fibo_recursive_five():
    """Тест числа Фибоначчи для пяти рекурсивно"""
    assert fibo_recursive(5) == 5


def test_fibo_recursive_ten():
    """Тест числа Фибоначчи для десяти рекурсивно"""
    assert fibo_recursive(10) == 55


def test_fibo_recursive_negative():
    """Тест числа Фибоначчи для отрицательного числа рекурсивно"""
    assert fibo_recursive(-1) == -1


def test_fibo_command_not_recursive(runner, shell_app, app_state):
    """Тест команды Фибоначчи без рекурсии"""
    result = runner.invoke(shell_app, ["fibo", "7"], obj=app_state)
    assert result.exit_code == 0
    assert "13" in result.output


def test_fibo_command_recursive(runner, shell_app, app_state):
    """Тест команды Фибоначчи с флагом рекурсии"""
    result = runner.invoke(shell_app, ["fibo", "7", "-r"], obj=app_state)
    assert result.exit_code == 0
    assert "13" in result.output


def test_fibo_command_negative(runner, shell_app, app_state):
    """Тест команды Фибоначчи для отрицательного числа"""
    result = runner.invoke(shell_app, ["fibo", "-1"], obj=app_state)
    assert "-1: Числа Фибоначчи, меньшего нуля, не существует" in result.output


def test_fibo_command_recursive_error(runner, shell_app, app_state):
    """Тест ошибки глубины рекурсии"""
    result = runner.invoke(shell_app, ["fibo", "1000", "-r"], obj=app_state)
    assert result.exit_code == 0
    assert "-1" in result.output
