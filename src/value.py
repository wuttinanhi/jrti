# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring


from src.util import parse_value
from src.variable import Variable
from src.variable_storage import VariableStorage


class Value:
    def __init__(self, value: any) -> None:
        self.__value = parse_value(value)

    def get(self, variable_storage: VariableStorage):
        if isinstance(self.__value, Variable):
            return self.__value.get_value(variable_storage)
        return self.__value

    def __repr__(self) -> str:
        return f"<Value value={self.__value}>"
