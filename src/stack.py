"""
Класс стека
Поддерживает функции push, pop, is_empty, peek,
clear, min
"""

from .errors import InvalidStackOperation


class Stack:
    def __init__(self) -> None:
        self._data: list[int] = []
        self._min_data: list[int] = []

    def push(self, x: int) -> None:
        self._data.append(x)
        if self._min_data:
            self._min_data.append(min(x, self._min_data[-1]))
        else:
            self._min_data.append(x)

    def pop(self) -> int:
        if not self._data:
            raise InvalidStackOperation(
                "Извлечение элемента из пустого стека.")
        self._min_data.pop()
        return self._data.pop()

    def is_empty(self) -> bool:
        return not self._data

    def __len__(self) -> int:
        return len(self._data)

    def peek(self) -> int:
        return self._data[-1]

    def min(self) -> int:
        if not self._min_data:
            raise InvalidStackOperation(
                "Извлечение элемента из пустого стека.")
        return self._min_data[-1]

    def clear(self) -> None:
        self._data = []
        self._min_data = []

    def print(self) -> None:
        print(self._data)
