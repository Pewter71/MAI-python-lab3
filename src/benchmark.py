"""
Функции бенчмарка.
"""
import time
from typing import Callable, Dict


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
            exec_time = timeit_once(algo_func, arr_copy)
            results[arr_name][algo_name] = exec_time
            print(f"{algo_name}: {exec_time:.6f} сек")

    return results
