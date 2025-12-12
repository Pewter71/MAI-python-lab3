"""
Тесты проверки сортировок
"""
from src.sorts import (
    bubble_sort, counting_sort, quick_sort,
    radix_sort, bucket_sort, heap_sort
)


def test_bubble_sort_empty():
    """Тест пузырьковой сортировки пустого массива"""
    assert bubble_sort([]) == []


def test_bubble_sort_single_element():
    """Тест пузырьковой сортировки одного элемента"""
    assert bubble_sort([5]) == [5]


def test_bubble_sort_sorted():
    """Тест пузырьковой сортировки отсортированного массива"""
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_bubble_sort_reverse():
    """Тест пузырьковой сортировки обратно отсортированного массива"""
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_bubble_sort_random():
    """Тест пузырьковой сортировки случайного массива"""
    assert bubble_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]


def test_counting_sort_empty():
    """Тест сортировки подсчетом пустого массива"""
    assert counting_sort([]) == []


def test_counting_sort_single_element():
    """Тест сортировки подсчетом одного элемента"""
    assert counting_sort([5]) == [5]


def test_counting_sort_with_duplicates():
    """Тест сортировки подсчетом с дубликатами"""
    assert counting_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]


def test_counting_sort_negative():
    """Тест сортировки подсчетом с отрицательными числами"""
    assert counting_sort([-3, -1, -4, 0, 2]) == [-4, -3, -1, 0, 2]


def test_quick_sort_empty():
    """Тест быстрой сортировки пустого массива"""
    assert quick_sort([]) == []


def test_quick_sort_single_element():
    """Тест быстрой сортировки одного элемента"""
    assert quick_sort([5]) == [5]


def test_quick_sort_random():
    """Тест быстрой сортировки случайного массива"""
    assert quick_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]


def test_quick_sort_floats():
    """Тест быстрой сортировки массива с float"""
    assert quick_sort([3.5, 1.2, 4.8, 2.1]) == [1.2, 2.1, 3.5, 4.8]


def test_radix_sort_empty():
    """Тест поразрядной сортировки пустого массива"""
    assert radix_sort([]) == []


def test_radix_sort_single_element():
    """Тест поразрядной сортировки одного элемента"""
    assert radix_sort([5]) == [5]


def test_radix_sort_random():
    """Тест поразрядной сортировки случайного массива"""
    assert radix_sort([170, 45, 75, 90, 802, 24, 2, 66]) == [
        2, 24, 45, 66, 75, 90, 170, 802]


def test_bucket_sort_empty():
    """Тест блочной сортировки пустого массива"""
    assert bucket_sort([]) == []


def test_bucket_sort_floats():
    """Тест блочной сортировки массива с float"""
    result = bucket_sort([0.78, 0.17, 0.39, 0.26, 0.72,
                         0.94, 0.21, 0.12, 0.23, 0.68])
    assert result == sorted(
        [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68])


def test_heap_sort_empty():
    """Тест пирамидальной сортировки пустого массива"""
    assert heap_sort([]) == []


def test_heap_sort_single_element():
    """Тест пирамидальной сортировки одного элемента"""
    assert heap_sort([5]) == [5]


def test_heap_sort_random():
    """Тест пирамидальной сортировки случайного массива"""
    assert heap_sort([3, 1, 4, 1, 5, 9, 2, 6]) == [1, 1, 2, 3, 4, 5, 6, 9]


def test_sort_command_bubble(runner, shell_app, app_state):
    """Тест команды сортировки алгоритмом пузырька"""
    result = runner.invoke(
        shell_app, ["sort", "bubble", "[5,2,8,1]"], obj=app_state)
    assert result.exit_code == 0
    assert "[1, 2, 5, 8]" in result.output


def test_sort_command_quick(runner, shell_app, app_state):
    """Тест команды быстрой сортировки"""
    result = runner.invoke(
        shell_app, ["sort", "quick", "[5,2,8,1]"], obj=app_state)
    assert result.exit_code == 0
    assert "[1, 2, 5, 8]" in result.output


def test_sort_command_invalid_input(runner, shell_app, app_state):
    """Тест команды сортировки с невалидным вводом"""
    result = runner.invoke(
        shell_app, ["sort", "bubble", "[a,b,c]"], obj=app_state)
    assert "Не удалось преобразовать" in result.output


def test_sort_command_bucket_invalid_range(runner, shell_app, app_state):
    """Тест команды сортировки bucket с невалидным массивом"""
    result = runner.invoke(
        shell_app, ["sort", "bucket", "[0.1, 100]"], obj=app_state)
    assert "Для этой сортировки могут использоваться числа <1 и >=0" in result.output
