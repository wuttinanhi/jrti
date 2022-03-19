# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,unused-private-member

from src.variable_storage import VariableStorage


class Variable:
    def __init__(self, name: str) -> None:
        self.__name = name

    def get_name(self):
        return self.__name

    def get_value(self, variable_storage: VariableStorage):
        return variable_storage.get(self.get_name())

    def __repr__(self) -> str:
        return f'<Variable name={self.__name}>'
