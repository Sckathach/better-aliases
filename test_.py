import pytest
import app

commands = [
    ('git init', 'git init'),
    ('git logadog', 'git log --all --decorate --oneline'),
    ('git logadog plus', 'git log --all --decorate --oneline --graph')
]

config = app.load_config(app.CONFIG_FILE)


@pytest.mark.parametrize('command, expected', commands)
def test_command(command, expected):
    assert app.craft_command(command.split(), config) == expected
