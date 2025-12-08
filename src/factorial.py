"""
Функции вычисления факториала числа.
Принимает неотрицательное число.
"""
import typer


def factorial_not_recursive(n: int) -> int:
    """Нерекурсивная реализация"""
    factorial_list = [1, 1, 2]
    if n < 0:
        return -1
    elif n < 3:
        return factorial_list[n]
    else:
        for index in range(3, n+1):
            factorial_list.append(factorial_list[index-1] * index)
        return factorial_list[n]


def factorial_recursive(n: int) -> int:
    """Рекурсивная реализация"""
    factorial_list = [1, 1, 2]
    if n < 0:
        return -1
    elif n < 3:
        return factorial_list[n]
    else:
        return factorial_recursive(n-1) * n


def factorial(n: int, r_flag:
              bool = typer.Option(
        False,
        "-r",
        "--recursive",
        help="Рекурсивное вычисление",),):
    """Вычисление факториала числа"""
    if n < 0:
        print(f"{n}: Факториала числа, меньшего нуля, не существует")
    else:
        if r_flag:
            result = factorial_recursive(n)
        else:
            result = factorial_not_recursive(n)
        print(result)
