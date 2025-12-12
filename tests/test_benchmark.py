"""
Тесты проверки функций вычисления числа Фибоначчи
"""
from src.benchmark import timeit_once
from src.sorts import bubble_sort
from src.generate_tests import rand_int_array
import time


def test_benchmark_timeit():
    """Тест вычисления времени работы одной функции"""
    test_list = rand_int_array(1000, 0, 1000)
    result = timeit_once(bubble_sort, test_list)
    assert result > 0


def test_benchmark_timeit_generic():
    """Тест проверки правильности вычисления времени работы одной функции"""
    def test_func():
        time.sleep(0.1)
    result = timeit_once(test_func)
    assert 0.09 < result < 0.11


def test_benchmark_command(runner, shell_app, app_state):
    """Тест работы бенчмарка"""
    result1 = runner.invoke(shell_app, ["benchmark", "555"], obj=app_state)
    result2 = runner.invoke(shell_app, ["benchmark", "555"], obj=app_state)

    assert result1.exit_code == 0
    assert result2.exit_code == 0
