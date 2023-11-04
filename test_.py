import pytest
import app

commands = [
    ('git init', 'git init'),
    ('git log', 'git log --all --decorate --oneline --graph'),
    ('a perf', 'asusctl profile -P Performance'),
    ('docker', 'docker'),
    ('f rouge', 'redshift -P -O 1000')
]

config = app.load_config(app.CONFIG_FILE)


@pytest.mark.parametrize('command, expected', commands)
def test_command(command, expected):
    assert app.craft_command(command.split(), config) == expected
