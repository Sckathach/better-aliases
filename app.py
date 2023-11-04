#! /usr/bin/python

from flask import Flask
import subprocess
import yaml
import sys
import os

ABS_PATH = os.path.dirname(__file__)
CONFIG_FILE = 'config_aliases.yaml'
ALL_KEYWORD = 'all'


def load_config(config_file):
    with open(ABS_PATH + '/' + config_file, "r") as file:
        config = yaml.safe_load(file)
    return config


def craft_command(x, config):
    buffer = ''
    args = ''
    c = config['commands']
    if len(x) > 0 and x[0] in c.keys():
        c = c[x[0]]
        if isinstance(c, dict) and ALL_KEYWORD in c.keys():
            buffer += c[ALL_KEYWORD] + ' '
        if len(x) > 1 and isinstance(c, dict) and x[1] in c.keys():
            c = c[x[1]]
            # print(c)
            if isinstance(c, dict) and ALL_KEYWORD in c.keys():
                buffer += c[ALL_KEYWORD] + ' '
            else:
                args = str(c)
            if len(x) > 2 and isinstance(c, dict) and x[2] in c.keys():
                c = c[x[2]]
                if isinstance(c, dict) and ALL_KEYWORD in c.keys():
                    buffer += c[ALL_KEYWORD] + ' '
                else:
                    buffer += c + ' '
                args += ' '.join(x[3:])
            else:
                # buffer += str(c) + ' '
                args += ' '.join(x[2:])
        else:
            # buffer += c + ' '
            args += ' '.join(x[1:])
    else:
        args += ' '.join(x)
    y = buffer + args
    if y[-1] == ' ':
        return y[:-1]
    else:
        return y


if __name__ == "__main__":
    # if len(sys.argv) < 3:
    #     print("Usage: python custom_script.py <config_file> <command>")
    #     sys.exit(1)

    config = load_config(CONFIG_FILE)
    x = sys.argv[1:]
    command = craft_command(x, config)
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
