# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,unused-private-member


from src.instruction.instruction import Instruction
from src.value import Value


class MathInstruction(Instruction):
    def __init__(self, key: str, op: str, value: Value) -> None:
        super().__init__()
        self.__key = key
        self.__op = op
        self.__value = value

    def run(self):
        variable_storage = self.get_variable_storage()
        original_value = variable_storage.get(self.__key)

        if self.__op == "+":
            variable_storage.set(
                self.__key, original_value +
                self.__value.get(self.get_variable_storage())
            )
        if self.__op == "-":
            variable_storage.set(
                self.__key, original_value -
                self.__value.get(self.get_variable_storage())
            )
        if self.__op == "*":
            variable_storage.set(
                self.__key, original_value *
                self.__value.get(self.get_variable_storage())
            )
        if self.__op == "/":
            variable_storage.set(
                self.__key, original_value /
                self.__value.get(self.get_variable_storage())
            )

    def __repr__(self) -> str:
        return f'<AddInstruction key={self.__key} op={self.__op}>'
