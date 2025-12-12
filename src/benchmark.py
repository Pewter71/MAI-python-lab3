"""
Функции бенчмарка
"""
import time
from typing import Callable, Dict, Any
from .sorts import bubble_sort, counting_sort, quick_sort, radix_sort, \
    bucket_sort, heap_sort
from .generate_tests import rand_int_array, rand_float_array, nearly_sorted, \
    reverse_sorted, many_duplicates
import typer


def timeit_once(func: Callable, *args, **kwargs) -> float:
    """
    Замеряет время выполнения одного вызова функции
    Возвращает время в секундах
    """
    start_time = time.perf_counter()
    func(*args, **kwargs)
    end_time = time.perf_counter()
    return end_time - start_time


def benchmark_sorts(arrays: Dict[str, list], algos: Dict[str, Callable]) -> Dict[str, Dict[str, float]]:
    """
    Запускает каждый алгоритм на копии каждого массива
    """
    results: Dict[str, Dict[str, float]] = {}

    for arr_name, original_arr in arrays.items():
        results[arr_name] = {}
        for algo_name, algo_func in algos.items():
            arr_copy = original_arr.copy()
            exec_time = timeit_once(algo_func, arr_copy) * 1000
            results[arr_name][algo_name] = exec_time

    return results


def benchmark(seed: int = typer.Argument(0,
                                         help="Seed генерации")):
    """
    Выводит результаты работы бенчмарка
    """
    algos: Dict[str, Callable[..., Any]] = {
        "bubble": bubble_sort,
        "counting": counting_sort,
        "quick": quick_sort,
        "radix": radix_sort,
        "heap": heap_sort
    }
    arrays: Dict[str, list] = {}
    arrays["ints"] = rand_int_array(900, -1000, 1000, seed=seed)
    arrays["duplicates"] = many_duplicates(900, 500, seed=seed)
    arrays["reverse"] = reverse_sorted(900)
    arrays["nearly"] = nearly_sorted(900, 100, seed=seed)
    result = benchmark_sorts(arrays, algos)
    for arr_name in arrays:
        print(arr_name)
        for algo_name in algos:
            print(f"{algo_name}: {result[arr_name][algo_name]:.6f} сек")
        print()
    algos_bucket: Dict[str, Callable[..., Any]] = {"bucket": bucket_sort}
    arrays_bucket: Dict[str, list] = {}
    arrays_bucket["floats"] = rand_float_array(900, 0, 1, seed=seed)
    result_bucket = benchmark_sorts(arrays_bucket, algos_bucket)
    for arr_name in arrays_bucket:
        print(arr_name)
        for algo_name in algos_bucket:
            print(f"{algo_name}: {result_bucket[arr_name][algo_name]:.6f} сек")
