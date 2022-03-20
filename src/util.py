# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

from src.variable import Variable


class Util:
    @staticmethod
    def is_number(value: any):
        try:
            float(value)
        except ValueError:
            return False
        return True

    @staticmethod
    def parse_number(value: str):
        try:
            return int(value)
        except ValueError:
            return float(value)

    @staticmethod
    def parse_value(value: any):
        if str(value).startswith("$") is True:
            return Variable(value)
        if str(value).startswith('"') and str(value).endswith('"') is True:
            return str(value)[1:-1]
        if Util.is_number(value) is True:
            return Util.parse_number(value)
        return str(value)
