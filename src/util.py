# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

from src.variable import Variable


def is_number(value: any):
    try:
        float(value)
    except ValueError:
        return False
    return True


def parse_number(value: str):
    try:
        return int(value)
    except ValueError:
        return float(value)


def parse_value(value: any):
    if str(value).startswith("$") is True:
        return Variable(value)
    if str(value).startswith('"') is True:
        return str(value)[1:-1]
    if is_number(value) is True:
        return parse_number(value)
    return str(value)
