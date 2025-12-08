"""
Функция вычисления числа Фибоначчи.
Принимает неотрицательное число.
"""
import typer


def fibo_not_recursive(n: int) -> int:
    """Нерекурсивная реализация"""
    fibo_list = [0, 1, 1]
    if n < 0:
        return -1
    elif n < 3:
        return fibo_list[n]
    else:
        for index in range(3, n+1):
            fibo_list.append(fibo_list[index-1] + fibo_list[index-2])
        return fibo_list[n]


def fibo_recursive(n: int) -> int:
    """Рекурсивная реализация"""
    fibo_list = [0, 1, 1]
    if n < 0:
        return -1
    elif n < 3:
        return fibo_list[n]
    else:
        return fibo_recursive(n-1) + fibo_recursive(n-2)


def fibo(n: int, r_flag:
         bool = typer.Option(
        False,
        "-r",
        "--recursive",
        help="Рекурсивное вычисление",),):
    """Вычисление n-ого числа Фибоначчи"""
    if n < 0:
        print(f"{n}: Числа Фибоначчи, меньшего нуля, не существует")
    else:
        if r_flag:
            result = fibo_recursive(n)
        else:
            result = fibo_not_recursive(n)
        print(result)
