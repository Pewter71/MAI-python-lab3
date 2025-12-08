"""
Функция запуска терминала.
"""

import shlex
import typer

from . import factorial, fibo, sorts, stack_commands
from .state import AppState


class InteractiveShell:
    def __init__(self):
        self.app = typer.Typer(no_args_is_help=True, add_completion=False)

        @self.app.callback()
        def init(ctx: typer.Context):
            if ctx.obj is None:
                ctx.obj = self.state

        self.app.command()(factorial.factorial)
        self.app.command()(fibo.fibo)
        self.app.command()(sorts.sort)
        self.app.command()(stack_commands.stack_checkout)
        self.app.command()(stack_commands.stack_push)
        self.app.command()(stack_commands.stack_pop)
        self.app.command()(stack_commands.stack_new)
        self.app.command()(stack_commands.stack_list)
        self.app.command()(stack_commands.stack_remove)
        self.app.command()(stack_commands.stack_min)
        self.app.command()(stack_commands.stack_size)
        self.app.command()(stack_commands.stack_show)
        self.app.command()(stack_commands.stack_clear)
        self.app.command()(stack_commands.stack_current)
        self.state = AppState(
            stack_list=[], current_stack=-1, stack_list_size=0,)

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
