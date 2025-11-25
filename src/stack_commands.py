import typer


def stack_push(ctx: typer.Context, n: int):
    ctx.obj.current_stack.push(n)


def stack_pop(ctx: typer.Context):
    ctx.obj.current_stack.pop()
