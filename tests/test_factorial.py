"""
Тесты проверки функций факториала
"""
from src.factorial import factorial_not_recursive, factorial_recursive


def test_factorial_not_recursive_zero():
    """Тест факториала нуля нерекурсивно"""
    assert factorial_not_recursive(0) == 1


def test_factorial_not_recursive_one():
    """Тест факториала единицы нерекурсивно"""
    assert factorial_not_recursive(1) == 1


def test_factorial_not_recursive_five():
    """Тест факториала пяти нерекурсивно"""
    assert factorial_not_recursive(5) == 120


def test_factorial_not_recursive_ten():
    """Тест факториала десяти нерекурсивно"""
    assert factorial_not_recursive(10) == 3628800


def test_factorial_not_recursive_negative():
    """Тест факториала отрицательного числа нерекурсивно"""
    assert factorial_not_recursive(-1) == -1


def test_factorial_recursive_zero():
    """Тест факториала нуля рекурсивно"""
    assert factorial_recursive(0) == 1


def test_factorial_recursive_one():
    """Тест факториала единицы рекурсивно"""
    assert factorial_recursive(1) == 1


def test_factorial_recursive_five():
    """Тест факториала пяти рекурсивно"""
    assert factorial_recursive(5) == 120


def test_factorial_recursive_ten():
    """Тест факториала десяти рекурсивно"""
    assert factorial_recursive(10) == 3628800


def test_factorial_recursive_negative():
    """Тест факториала отрицательного числа рекурсивно"""
    assert factorial_recursive(-1) == -1


def test_factorial_command_not_recursive(runner, shell_app, app_state):
    """Тест команды факториала без рекурсии"""
    result = runner.invoke(shell_app, ["factorial", "5"], obj=app_state)
    assert result.exit_code == 0
    assert "120" in result.output


def test_factorial_command_recursive(runner, shell_app, app_state):
    """Тест команды факториала с флагом рекурсии"""
    result = runner.invoke(shell_app, ["factorial", "5", "-r"], obj=app_state)
    assert result.exit_code == 0
    assert "120" in result.output


def test_factorial_command_negative(runner, shell_app, app_state):
    """Тест команды факториала для отрицательного числа"""
    result = runner.invoke(shell_app, ["factorial", "-1"], obj=app_state)
    assert "-1: Факториала числа, меньшего нуля, не существует" in result.output


def test_factorial_command_recursive_error(runner, shell_app, app_state):
    """Тест ошибки глубины рекурсии"""
    result = runner.invoke(
        shell_app, ["factorial", "1000", "-r"], obj=app_state)
    assert result.exit_code == 0
    assert "-1" in result.output
