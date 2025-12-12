"""
Общие fixtures для тестов
"""
import pytest
from typer.testing import CliRunner
from src.main import InteractiveShell
from src.state import AppState


@pytest.fixture
def runner():
    return CliRunner()


@pytest.fixture
def shell_app():
    shell = InteractiveShell()
    return shell.app


@pytest.fixture
def app_state():
    return AppState(stack_list=[], current_stack=-1, stack_list_size=0, generated_list=[])
