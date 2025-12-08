"""
Консольные команды для управления стеками.
"""
import typer
from .stack import Stack


def stack_push(ctx: typer.Context, number: int):
    """Добавить элемент в стек"""
    if ctx.obj.current_stack == -1:
        print("Не создано ни одного стека")
    else:
        ctx.obj.stack_list[ctx.obj.current_stack-1].push(number)
        print(f"Добавлен элемент {number} в стек {ctx.obj.current_stack}")


def stack_pop(ctx: typer.Context):
    """Берет элемент из стека"""
    if ctx.obj.current_stack == -1:
        print("Не создано ни одного стека")
    else:
        element = ctx.obj.stack_list[ctx.obj.current_stack-1].pop()
        print(f"Из стека {ctx.obj.current_stack} был взят: {element}")


def stack_new(ctx: typer.Context):
    """Создать новый стек"""
    ctx.obj.stack_list.append(Stack())
    if ctx.obj.current_stack == -1:
        ctx.obj.current_stack = 1
    ctx.obj.stack_list_size += 1
    print(f"Создан стек {ctx.obj.stack_list_size}")


def stack_current(ctx: typer.Context):
    """Выводит номер текущего стека"""
    print(f"Сейчас выбран стек {ctx.obj.current_stack}")


def stack_list(ctx: typer.Context):
    """Список стеков"""
    stacks = ctx.obj.stack_list
    stacks_count = len(stacks)
    print(f"Всего {stacks_count} стекs")
    for stack in stacks:
        stack.print()


def stack_checkout(ctx: typer.Context, number: int):
    """Переключиться на стек"""
    size = ctx.obj.stack_list_size
    if size >= number and number > 0:
        ctx.obj.current_stack = number
        print(f"Выбран стек {ctx.obj.current_stack}")
    else:
        print("Стека под указанным номером не существует")


def stack_remove(ctx: typer.Context, number: int = typer.Option(None)):
    """Удалить стек"""
    size = ctx.obj.stack_list_size
    if number is None:
        number = ctx.obj.current_stack
    if size >= number and number > 0:
        del ctx.obj.stack_list.pop[number-1]
        ctx.obj.stack_list_size -= 1
        if ctx.obj.stack_list_size == 0:
            ctx.obj.stack_current = -1
        print(f"Стек {number} удален")
    else:
        print("Стека под указанным номером не существует")


def stack_min(ctx: typer.Context, number: int = typer.Option(None)):
    """Получить минимум из стека"""
    size = ctx.obj.stack_list_size
    if number is None:
        number = ctx.obj.current_stack
    if size >= number and number > 0:
        print(ctx.obj.stack_list[number-1].min())
    else:
        print("Стека под указанным номером не существует")


def stack_size(ctx: typer.Context, number: int = typer.Option(None)):
    """Вывести размер стека"""
    size = ctx.obj.stack_list_size
    if number is None:
        number = ctx.obj.current_stack
    if size >= number and number > 0:
        print(
            f"В стеке {number} находятся {len(ctx.obj.stack_list[number-1])} элементs")
    else:
        print("Стека под указанным номером не существует")


def stack_show(ctx: typer.Context, number: int = typer.Option(None)):
    """Вывести стек"""
    size = ctx.obj.stack_list_size
    if number is None:
        number = ctx.obj.current_stack
    if size >= number and number > 0:
        ctx.obj.stack_list[number-1].print()
    else:
        print("Стека под указанным номером не существует")


def stack_clear(ctx: typer.Context, number: int = typer.Option(None)):
    """Очистить стек"""
    size = ctx.obj.stack_list_size
    if number is None:
        number = ctx.obj.current_stack
    if size >= number and number > 0:
        ctx.obj.stack_list[number-1].clear()
        print(f"Стек номер {number} очищен")
    else:
        print("Стека под указанным номером не существует")
