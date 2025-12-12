"""
Алгоритмы генерации массивов
"""
import random
from enum import Enum
import typer


class GenerateAlgorithm(str, Enum):
    integers = "integers"
    floats = "floats"
    nearly = "nearly"
    duplicates = "duplicates"
    reverse = "reverse"


def rand_int_array(n: int, lo: int, hi: int, *, distinct=False, seed=None) -> list[int]:
    """
    Генерирует массив из n случайных целых чисел в диапазоне [l, h]
    """
    if seed is not None:
        random.seed(seed)

    if distinct:
        return random.sample(range(lo, hi + 1), n)

    return [random.randint(lo, hi) for _ in range(n)]


def nearly_sorted(n: int, swaps: int, *, seed=None) -> list[int]:
    """
    Генерирует почти отсортированный массив
    """
    if seed is not None:
        random.seed(seed)

    arr = list(range(n))
    for _ in range(swaps):
        i, j = random.randint(0, n - 1), random.randint(0, n - 1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


def many_duplicates(n: int, k_unique=5, *, seed=None) -> list[int]:
    """
    Генерирует массив длины n, используя только k_unique уникальных чисел
    """
    if seed is not None:
        random.seed(seed)
    uniques = [random.randint(0, n) for _ in range(k_unique)]
    return [random.choice(uniques) for _ in range(n)]


def reverse_sorted(n: int) -> list[int]:
    """
    Возвращает массив, отсортированный в обратном порядке
    """
    return list(range(n - 1, -1, -1))


def rand_float_array(n: int, lo=0.0, hi=1.0, *, seed=None) -> list[float]:
    """
    Генерирует массив float
    По умолчанию [0.0, 1.0)
    """
    if seed is not None:
        random.seed(seed)
    return [random.uniform(lo, hi) for _ in range(n)]


def generate_integers(
    ctx: typer.Context,
    n: int = typer.Argument(...,
                            help="Количество элементов списка"),
    lo: int = typer.Argument(...,
                             help="Наибольший элемент списка"),
    hi: int = typer.Argument(...,
                             help="Наименьший элемент списка"),
    distinct: bool = typer.Option(
        False, "--distinct", "-d", help="Уникальные элементы"),
    seed: int | None = typer.Option(
        None, "--seed", "-s", help="Seed для генератора")
):
    """
    Генерирует список целых чисел в выбранном диапазоне
    """
    result = rand_int_array(n, lo, hi, distinct=distinct, seed=seed)
    ctx.obj.generated_list = result
    print(f"Сгенерирован список: {result}")


def generate_floats(
    ctx: typer.Context,
    n: int = typer.Argument(...,
                            help="Количество элементов списка"),
    lo: float = typer.Argument(...,
                               help="Наибольший элемент списка"),
    hi: float = typer.Argument(...,
                               help="Наименьший элемент списка"),
    seed: int | None = typer.Option(
        None, "--seed", "-s", help="Seed для генератора")
):
    """
    Генерирует список вещественных чисел в выбранном диапазоне
    """
    result = rand_float_array(n, lo, hi, seed=seed)
    ctx.obj.generated_list = result
    print(f"Сгенерирован список: {result}")


def generate_nearly(
    ctx: typer.Context,
    n: int = typer.Argument(...,
                            help="Количество элементов списка"),
    swaps: int = typer.Argument(...,
                                help="Количество перестановок"),
    seed: int | None = typer.Option(
        None, "--seed", "-s", help="Seed для генератора")
):
    """
    Генерирует почти отсортированный список
    """
    result = nearly_sorted(n, swaps, seed=seed)
    ctx.obj.generated_list = result
    print(f"Сгенерирован список: {result}")


def generate_duplicates(
    ctx: typer.Context,
    n: int = typer.Argument(...,
                            help="Количество элементов списка"),
    k_unique: int = typer.Argument(...,
                                   help="Количество уникальных чисел"),
    seed: int | None = typer.Option(
        None, "--seed", "-s", help="Seed для генератора")
):
    """
    Генерирует список с дубликатами
    """
    result = many_duplicates(n, k_unique, seed=seed)
    ctx.obj.generated_list = result
    print(f"Сгенерирован список: {result}")


def generate_reverse(
    ctx: typer.Context,
    n: int = typer.Argument(...,
                            help="Количество элементов списка")
):
    """
    Генерирует список отсортированный наоборот
    """
    result = reverse_sorted(n)
    ctx.obj.generated_list = result
    print(f"Сгенерирован список: {result}")


def generate_show(ctx: typer.Context):
    """
    Выводит последний сгенерированный список
    """
    print(ctx.obj.generated_list)
