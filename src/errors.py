"""Пользовательские ошибки"""


class InvalidStackOperation(Exception):
    """Неправильная работа со стеком."""

    def __init__(self, message: str):
        super().__init__(message)
