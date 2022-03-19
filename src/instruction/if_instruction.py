# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,line-too-long,invalid-name


from typing import Dict
from src.instruction.instruction import Instruction
from src.value import Value


class IfInstruction(Instruction):
    def __init__(
        self,
        a: Value,
        condition: str,
        b: Value,
        if_true_goto: str
    ) -> None:
        super().__init__()
        self.__a = a
        self.__condition = condition
        self.__b = b
        self.__true_goto = if_true_goto

    def eval(self):
        a = self.__a.get(self.get_variable_storage())
        b = self.__b.get(self.get_variable_storage())

        if self.__condition == "==":
            return a == b
        if self.__condition == ">":
            return a > b
        if self.__condition == "<":
            return a < b
        if self.__condition == ">=":
            return a >= b
        if self.__condition == "<=":
            return a <= b
        if self.__condition == "!=":
            return a != b

    def get_goto(self, goto_dict: Dict[str, int]):
        if self.eval() is False:
            return None
        return goto_dict.get(self.__true_goto)

    def __repr__(self) -> str:
        return f'<IfInstruction a={self.__a} b={self.__b} condition={self.__condition} true={self.__true_goto}>'
