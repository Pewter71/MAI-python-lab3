"""
Тесты работы стека
"""
import pytest
from src.stack import Stack
from src.errors import InvalidStackOperation


def test_stack_push_single():
    """Тест добавления одного элемента"""
    stack = Stack()
    stack.push(5)
    assert len(stack) == 1
    assert stack.peek() == 5


def test_stack_push_multiple():
    """Тест добавления нескольких элементов"""
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert len(stack) == 3
    assert stack.peek() == 3


def test_stack_pop():
    """Тест извлечения элемента"""
    stack = Stack()
    stack.push(5)
    stack.push(10)
    element = stack.pop()
    assert element == 10
    assert len(stack) == 1


def test_stack_pop_empty():
    """Тест ошибки при извлечении из пустого стека"""
    stack = Stack()
    with pytest.raises(InvalidStackOperation):
        stack.pop()


def test_stack_is_empty_true():
    """Тест проверки что стек пуст"""
    stack = Stack()
    assert stack.is_empty() is True


def test_stack_is_empty_false():
    """Тест проверки что стек не пуст"""
    stack = Stack()
    stack.push(1)
    assert stack.is_empty() is False


def test_stack_min():
    """Тест минимума"""
    stack = Stack()
    stack.push(5)
    stack.push(2)
    stack.push(8)
    stack.push(1)
    assert stack.min() == 1


def test_stack_min_after_pop():
    """Тест обновления минимума"""
    stack = Stack()
    stack.push(5)
    stack.push(2)
    stack.push(1)
    stack.pop()
    assert stack.min() == 2


def test_stack_clear():
    """Тест очистки"""
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.clear()
    assert len(stack) == 0
    assert stack.is_empty() is True


def test_stack_peek():
    """Тест просмотра вершины стека"""
    stack = Stack()
    stack.push(10)
    stack.push(20)
    assert stack.peek() == 20
    assert len(stack) == 2
