"""
Алгоритмы сортировок
"""
from enum import Enum
import typer
from typing import TypeVar

T = TypeVar('T', int, float)


class SortAlgorithm(str, Enum):
    bubble = "bubble"
    counting = "counting"
    quick = "quick"
    radix = "radix"
    bucket = "bucket"
    heap = "heap"


def bubble_sort(a: list[int]) -> list[int]:
    """Реализация сортировки пузырьком"""
    list_size = len(a)
    sorted_list = a.copy()
    for i in range(list_size):
        for j in range(0, list_size-i-1):
            if sorted_list[j] > sorted_list[j+1]:
                sorted_list[j], sorted_list[j +
                                            1] = sorted_list[j+1], sorted_list[j]
    return sorted_list


def counting_sort(a: list[int]) -> list[int]:
    """Реализация сортировки подсчетом"""
    count_dict = dict()
    sorted_list: list[int] = []
    if len(a) == 0:
        return sorted_list
    min_element = a[0]
    max_element = a[0]
    for i in a:
        if i not in count_dict:
            count_dict[i] = 1
        else:
            count_dict[i] += 1
        min_element = min(min_element, i)
        max_element = max(max_element, i)
    for i in range(min_element, max_element+1):
        if i in count_dict:
            sorted_list += [i] * count_dict[i]
    return sorted_list


def quick_sort(a: list[T]) -> list[T]:
    """Реализация быстрой сортировки"""
    if len(a) < 2:
        return a
    pivot = a[0]
    left = [x for x in a if x < pivot]
    middle = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def radix_sort(a: list[int], base: int = 10) -> list[int]:
    """Реализация поразрядной сортировки"""
    sorted_list = a.copy()
    if len(sorted_list) == 0:
        return sorted_list
    max_digits = max([len(str(x)) for x in sorted_list])
    base = 10
    bins: list[list[int]] = [[] for _ in range(base)]

    for i in range(0, max_digits):
        for x in sorted_list:
            digit = (x // base ** i) % base
            bins[digit].append(x)
        sorted_list = [x for queue in bins for x in queue]
        bins = [[] for _ in range(base)]
    return sorted_list


def bucket_sort(a: list[float],
                buckets_count: int | None = None) -> list[float]:
    sorted_list = a.copy()
    """Реализация блочной сортировки"""
    n = len(sorted_list)
    if buckets_count is not None:
        buckets: list[list[float]] = [[] for _ in range(buckets_count)]
        n = buckets_count
    else:
        buckets = [[] for _ in range(n)]
    for num in sorted_list:
        bi = int(n * num)
        buckets[bi].append(num)
    for i in range(len(buckets)):
        buckets[i] = quick_sort(buckets[i])
    index = 0
    for bucket in buckets:
        for num in bucket:
            sorted_list[index] = num
            index += 1
    return sorted_list


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(a: list[int]) -> list[int]:
    """Реализация пирамидальной сортировки"""
    sorted_list = a.copy()
    n = len(sorted_list)
    for i in range(n // 2 - 1, -1, -1):
        heapify(sorted_list, n, i)
    for i in range(n - 1, 0, -1):
        sorted_list[0], sorted_list[i] = sorted_list[i], sorted_list[0]
        heapify(sorted_list, i, 0)
    return sorted_list


def sort(ctx: typer.Context,
         sort_type: SortAlgorithm = typer.Argument(
             ..., help="Алгоритм сортировки"),
         input: str = typer.Argument(...,
                                     help="Список чисел в формате строки, например [5,1,3]")
         ):
    """
    Сортирует переданный список выбранным алгоритмом.
    """
    input_list = []
    if input == "gen":
        input_list = ctx.obj.generated_list
    else:
        clean_str = input.replace("[", "").replace("]", "").strip()
        if clean_str:
            try:
                input_list = [float(item.strip())
                              for item in clean_str.split(",")]
            except ValueError:
                print(
                    "Не удалось преобразовать данные в числа")
    result: list[int] | list[float] = []

    if sort_type == SortAlgorithm.bubble:
        data_int = [int(x) for x in input_list]
        result = bubble_sort(data_int)
    elif sort_type == SortAlgorithm.counting:
        data_int = [int(x) for x in input_list]
        result = counting_sort(data_int)
    elif sort_type == SortAlgorithm.quick:
        data_int = [int(x) for x in input_list]
        result = quick_sort(data_int)
    elif sort_type == SortAlgorithm.radix:
        data_int = [int(x) for x in input_list]
        result = radix_sort(data_int)
    elif sort_type == SortAlgorithm.bucket:
        if isinstance(input_list[0], int):
            print("Для этой сортировки не могут использоваться целые числа")
            return
        if max(input_list) >= 1 or min(input_list) < 0:
            print("Для этой сортировки могут использоваться числа <1 и >=0")
            return
        else:
            result = bucket_sort(input_list)
    elif sort_type == SortAlgorithm.heap:
        data_int = [int(x) for x in input_list]
        result = heap_sort(data_int)
    print(result)
