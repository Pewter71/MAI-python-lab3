"""
Тесты проверки команд стека
"""


def test_stack_new(runner, shell_app, app_state):
    """Тест создания нового стека"""
    result = runner.invoke(shell_app, ["stack-new"], obj=app_state)
    assert result.exit_code == 0
    assert "Создан стек 1" in result.output


def test_stack_push_no_stack(runner, shell_app, app_state):
    """Тест ошибки добавления в несуществующий стек"""
    result = runner.invoke(shell_app, ["stack-push", "5"], obj=app_state)
    assert "Ни один стек не выбран" in result.output


def test_stack_push_success(runner, shell_app, app_state):
    """Тест успешного добавления элемента в стек"""
    runner.invoke(shell_app, ["stack-new"], obj=app_state)
    runner.invoke(shell_app, ["stack-checkout",  "1"], obj=app_state)
    result = runner.invoke(shell_app, ["stack-push", "10"], obj=app_state)
    assert result.exit_code == 0
    assert "Добавлен элемент 10" in result.output


def test_stack_pop_no_stack(runner, shell_app, app_state):
    """Тест ошибки извлечения из несуществующего стека"""
    result = runner.invoke(shell_app, ["stack-pop"], obj=app_state)
    assert "Ни один стек не выбран" in result.output


def test_stack_pop_success(runner, shell_app, app_state):
    """Тест успешного извлечения элемента из стека"""
    runner.invoke(shell_app, ["stack-new"], obj=app_state)
    runner.invoke(shell_app, ["stack-checkout",  "1"], obj=app_state)
    runner.invoke(shell_app, ["stack-push", "20"], obj=app_state)
    result = runner.invoke(shell_app, ["stack-pop"], obj=app_state)
    assert result.exit_code == 0
    assert "был взят: 20" in result.output


def test_stack_list_multiple_stacks(runner, shell_app, app_state):
    """Тест вывода списка стеков"""
    runner.invoke(shell_app, ["stack-new"], obj=app_state)
    runner.invoke(shell_app, ["stack-new"], obj=app_state)
    result = runner.invoke(shell_app, ["stack-list"], obj=app_state)
    assert "Всего 2 стек" in result.output


def test_stack_checkout_valid(runner, shell_app, app_state):
    """Тест переключения на существующий стек"""
    runner.invoke(shell_app, ["stack-new"], obj=app_state)
    runner.invoke(shell_app, ["stack-new"], obj=app_state)
    result = runner.invoke(shell_app, ["stack-checkout", "2"], obj=app_state)
    assert "Выбран стек 2" in result.output


def test_stack_checkout_invalid(runner, shell_app, app_state):
    """Тест ошибки переключения на несуществующий стек"""
    runner.invoke(shell_app, ["stack-new"], obj=app_state)
    result = runner.invoke(shell_app, ["stack-checkout", "5"], obj=app_state)
    assert "не существует" in result.output


def test_stack_remove_by_number(runner, shell_app, app_state):
    """Тест удаления стека по номеру"""
    runner.invoke(shell_app, ["stack-new"], obj=app_state)
    result = runner.invoke(shell_app, ["stack-remove", "1"], obj=app_state)
    assert "Стек 1 удален" in result.output


def test_stack_remove_invalid(runner, shell_app, app_state):
    """Тест ошибки удаления несуществующего стека"""
    result = runner.invoke(shell_app, ["stack-remove", "1"], obj=app_state)
    assert "не существует" in result.output


def test_stack_min_success(runner, shell_app, app_state):
    """Тест получения минимального элемента из стека"""
    runner.invoke(shell_app, ["stack-new"], obj=app_state)
    runner.invoke(shell_app, ["stack-checkout",  "1"], obj=app_state)
    runner.invoke(shell_app, ["stack-push", "5"], obj=app_state)
    runner.invoke(shell_app, ["stack-push", "2"], obj=app_state)
    result = runner.invoke(shell_app, ["stack-min"], obj=app_state)
    assert "2" in result.output


def test_stack_size_success(runner, shell_app, app_state):
    """Тест получения размера стека"""
    runner.invoke(shell_app, ["stack-new"], obj=app_state)
    runner.invoke(shell_app, ["stack-checkout",  "1"], obj=app_state)
    runner.invoke(shell_app, ["stack-push", "1"], obj=app_state)
    runner.invoke(shell_app, ["stack-push", "2"], obj=app_state)
    result = runner.invoke(shell_app, ["stack-size"], obj=app_state)
    assert "2 элемент" in result.output


def test_stack_clear_success(runner, shell_app, app_state):
    """Тест очистки стека"""
    runner.invoke(shell_app, ["stack-new"], obj=app_state)
    runner.invoke(shell_app, ["stack-checkout",  "1"], obj=app_state)
    runner.invoke(shell_app, ["stack-push", "1"], obj=app_state)
    result = runner.invoke(shell_app, ["stack-clear"], obj=app_state)
    assert "очищен" in result.output


def test_stack_current(runner, shell_app, app_state):
    """Тест вывода номера текущего стека"""
    runner.invoke(shell_app, ["stack-new"], obj=app_state)
    result = runner.invoke(shell_app, ["stack-current"], obj=app_state)
    assert "Ни один стек не выбран" in result.output
