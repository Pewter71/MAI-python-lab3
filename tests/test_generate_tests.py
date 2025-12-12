"""
Тесты работы генераторов
"""
from src.generate_tests import (
    rand_int_array, nearly_sorted, many_duplicates,
    reverse_sorted, rand_float_array
)


def test_rand_int_array_length():
    """Тест длины"""
    arr = rand_int_array(10, 0, 100, seed=42)
    assert len(arr) == 10


def test_rand_int_array_range():
    """Тест диапазона значений"""
    arr = rand_int_array(100, 0, 10, seed=42)
    assert all(0 <= x <= 10 for x in arr)


def test_rand_int_array_distinct():
    """Тест генераци с уникальными элементами"""
    arr = rand_int_array(10, 0, 100, distinct=True, seed=42)
    assert len(arr) == len(set(arr))


def test_rand_int_array_seed_equal():
    """Тест воспроизводимости генерации с одинаковым seed"""
    arr1 = rand_int_array(10, 0, 100, seed=42)
    arr2 = rand_int_array(10, 0, 100, seed=42)
    assert arr1 == arr2


def test_nearly_sorted_length():
    """Тест длины почти отсортированного массива"""
    arr = nearly_sorted(20, 3, seed=42)
    assert len(arr) == 20


def test_nearly_sorted_zero_swaps():
    """Тест генерации полностью отсортированного массива"""
    arr = nearly_sorted(10, 0, seed=42)
    assert arr == list(range(10))


def test_nearly_sorted_seed_equal():
    """Тест воспроизводимости почти отсортированного массива"""
    arr1 = nearly_sorted(10, 3, seed=42)
    arr2 = nearly_sorted(10, 3, seed=42)
    assert arr1 == arr2


def test_many_duplicates_length():
    """Тест длины массива с дубликатами"""
    arr = many_duplicates(50, k_unique=5, seed=42)
    assert len(arr) == 50


def test_many_duplicates_unique_count():
    """Тест количества уникальных элементов"""
    arr = many_duplicates(100, k_unique=3, seed=42)
    assert len(set(arr)) == 3


def test_many_duplicates_seed_equal():
    """Тест воспроизводимости массива с дубликатами"""
    arr1 = many_duplicates(20, k_unique=5, seed=2)
    arr2 = many_duplicates(20, k_unique=5, seed=2)
    assert arr1 == arr2


def test_reverse_sorted():
    """Тест генерации обратно отсортированного массива"""
    arr = reverse_sorted(10)
    assert arr == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


def test_rand_float_array_length():
    """Тест длины массива с float"""
    arr = rand_float_array(10, seed=22)
    assert len(arr) == 10


def test_rand_float_array_range():
    """Тест диапазона значений float массива"""
    arr = rand_float_array(100, lo=0.0, hi=1.0, seed=42)
    assert all(0.0 <= x < 1.0 for x in arr)


def test_rand_float_array_seed_equal():
    """Тест воспроизводимости float массива"""
    arr1 = rand_float_array(10, seed=1)
    arr2 = rand_float_array(10, seed=1)
    assert arr1 == arr2


def test_generate_integers_command(runner, shell_app, app_state):
    """Тест команды генерации целых чисел"""
    result = runner.invoke(
        shell_app, ["generate-integers", "10", "0", "100"], obj=app_state)
    assert result.exit_code == 0
    assert f"Сгенерирован список: {app_state.generated_list}" in result.output
    assert len(app_state.generated_list) == 10


def test_generate_integers_with_distinct(runner, shell_app, app_state):
    """Тест команды генерации уникальных целых чисел"""
    result = runner.invoke(
        shell_app, ["generate-integers", "10", "0", "100", "-d"], obj=app_state
    )
    assert result.exit_code == 0
    assert len(set(app_state.generated_list)) == 10


def test_generate_integers_with_seed(runner, shell_app, app_state):
    """Тест команды генерации с seed"""
    result1 = runner.invoke(
        shell_app, ["generate-integers", "10", "0", "100", "-s", "42"], obj=app_state
    )
    list1 = app_state.generated_list.copy()

    result2 = runner.invoke(
        shell_app, ["generate-integers", "10", "0", "100", "-s", "42"], obj=app_state
    )
    list2 = app_state.generated_list
    assert result1.exit_code == 0
    assert result2.exit_code == 0
    assert list1 == list2


def test_generate_floats_command(runner, shell_app, app_state):
    """Тест команды генерации float"""
    result = runner.invoke(
        shell_app, ["generate-floats", "10", "10.0", "20.0"], obj=app_state
    )
    assert result.exit_code == 0
    assert f"Сгенерирован список: {app_state.generated_list}" in result.output
    assert all(10.0 <= x <= 20.0 for x in app_state.generated_list)


def test_generate_nearly_with_seed(runner, shell_app, app_state):
    """Тест команды генерации почти отсортированного массива с seed"""
    result = runner.invoke(
        shell_app, ["generate-nearly", "10", "3", "-s", "42"], obj=app_state
    )
    assert result.exit_code == 0
    assert f"Сгенерирован список: {app_state.generated_list}" in result.output


def test_generate_duplicates_command(runner, shell_app, app_state):
    """Тест команды генерации массива с дубликатами"""
    result = runner.invoke(
        shell_app, ["generate-duplicates", "50", "5"], obj=app_state)
    assert result.exit_code == 0
    assert len(app_state.generated_list) == 50
    assert len(set(app_state.generated_list)) <= 5


def test_generate_reverse_command(runner, shell_app, app_state):
    """Тест команды генерации обратно отсортированного массива"""
    result = runner.invoke(
        shell_app, ["generate-reverse", "10"], obj=app_state)
    assert result.exit_code == 0
    assert app_state.generated_list == [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    assert f"Сгенерирован список: {app_state.generated_list}" in result.output


def test_generate_show_command(runner, shell_app, app_state):
    """Тест команды вывода последнего сгенерированного списка"""
    runner.invoke(shell_app, ["generate-integers",
                  "5", "0", "10"], obj=app_state)
    result = runner.invoke(shell_app, ["generate-show"], obj=app_state)
    assert result.exit_code == 0
    assert str(app_state.generated_list) in result.output


def test_generate_show_empty(runner, shell_app, app_state):
    """Тест команды вывода без предварительной генерации"""
    app_state.generated_list = []
    result = runner.invoke(shell_app, ["generate-show"], obj=app_state)
    assert result.exit_code == 0
    assert "[]" in result.output
