"""
Хранит класс состояния приложения.
"""

from dataclasses import dataclass
from .stack import Stack


@dataclass
class AppState:
    current_stack: Stack
