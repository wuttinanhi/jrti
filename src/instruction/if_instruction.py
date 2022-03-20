# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,line-too-long,invalid-name


from typing import Dict
from src.instruction.instruction import Instruction
from src.value import Value


class IfInstruction(Instruction):
    def __init__(
        self,
        a: Value,
        compare: str,
        b: Value,
        if_true_goto: str
    ) -> None:
        super().__init__()
        self.__a = a
        self.__compare = compare
        self.__b = b
        self.__true_goto = if_true_goto

    def eval(self):
        a = self.__a.get(self.get_variable_storage())
        b = self.__b.get(self.get_variable_storage())
        compare = self.__compare
        result: bool = False

        if compare == "==":
            result = a == b
        if compare == ">":
            result = a > b
        if compare == "<":
            result = a < b
        if compare == ">=":
            result = a >= b
        if compare == "<=":
            result = a <= b
        if compare == "!=":
            result = a != b

        return result

    def get_goto(self, goto_dict: Dict[str, int]):
        if self.eval() is False:
            return None
        return goto_dict.get(self.__true_goto)

    def __repr__(self) -> str:
        return f'<IfInstruction a={self.__a} b={self.__b} compare={self.__compare} true_goto={self.__true_goto}>'
