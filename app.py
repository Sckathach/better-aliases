from flask import Flask
import os
import subprocess
import sys
import yaml

ABS_PATH = os.path.dirname(__file__)
CONFIG_FILE = 'config.yaml'
ALL_KEYWORD = 'all'


def load_config(config_file):
    with open(ABS_PATH + '/' + config_file, "r") as file:
        config = yaml.safe_load(file)
    return config


def craft_command(input, config):
    buffer = ''
    if len(input) > 0 and input[0] in config['commands'].keys():
        if isinstance(config['commands'][input[0]], dict) and ALL_KEYWORD in config['commands'][input[0]].keys():
            buffer += config['commands'][input[0]][ALL_KEYWORD] + ' '
        if len(input) > 1 and input[1] in config['commands'][input[0]].keys():
            if isinstance(config['commands'][input[0]][input[1]], dict) and ALL_KEYWORD in config['commands'][input[0]][input[1]].keys():
                buffer += config['commands'][input[0]][input[1]][ALL_KEYWORD] + ' '
            if len(input) > 2 and input[2] in config['commands'][input[0]][input[1]].keys():
                if isinstance(config['commands'][input[0]][input[1]][input[2]], dict) and ALL_KEYWORD in config['commands'][input[0]][input[1]][input[2]].keys():
                    buffer += config['commands'][input[0]][input[1]][input[2]][ALL_KEYWORD] + ' '
                else:
                    buffer += config['commands'][input[0]][input[1]][input[2]] + ' '
                args = ' '.join(input[3:])
            else:
                args = ' '.join(input[2:])
        else:
            args = ' '.join(input[1:])
    else:
        args = ' '.join(input)
    return buffer + args


if __name__ == "__main__":
    # if len(sys.argv) < 3:
    #     print("Usage: python custom_script.py <config_file> <command>")
    #     sys.exit(1)

    config = load_config(CONFIG_FILE)
    input = sys.argv[1:]
    print(input)
    command = craft_command(input, config)
    print(command)

# app = Flask(__name__)
#
#
# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello World!'
#
#
# if __name__ == '__main__':
#     app.run()
