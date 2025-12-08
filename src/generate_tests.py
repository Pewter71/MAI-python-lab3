"""
Алгоритмы генерации массивов.
"""
import random


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
