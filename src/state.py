"""
Хранит класс состояния приложения.
"""

from dataclasses import dataclass
from .stack import Stack


@dataclass
class AppState:
    stack_list: list[Stack]
    current_stack: int
    stack_list_size: int
