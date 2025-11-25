"""
Функция запуска терминала.
"""

import shlex
import typer

from . import factorial, fibo
from .state import AppState
from .stack import Stack


class InteractiveShell:
    def __init__(self):
        self.app = typer.Typer(no_args_is_help=True, add_completion=False)

        @self.app.callback()
        def init(ctx: typer.Context):
            if ctx.obj is None:
                ctx.obj = self.state

        self.app.command()(factorial.factorial)
        self.app.command()(fibo.fibo)

        self.state = AppState(current_stack=Stack())

    def run(self):
        typer.echo("Введите --help для показа команд.")
        typer.echo("Введите 'exit' для выхода.\n")

        while True:
            try:
                user_input = typer.prompt("Введите команду")

                if not user_input.strip():
                    continue

                if user_input.strip() == "exit":
                    break
                args = shlex.split(user_input)
                self.app(args, standalone_mode=False, obj=self.state)

            except Exception as e:
                typer.echo(f"Error: {e}")


def main():

    shell = InteractiveShell()
    shell.run()


if __name__ == "__main__":
    main()
