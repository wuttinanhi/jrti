# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring


from src.instruction.instruction import Instruction
from src.value import Value


class PrintInstruction(Instruction):
    def __init__(self, value: Value) -> None:
        super().__init__()
        self.__value = value

    def run(self):
        print(self.__value.get(self.get_variable_storage()), end="")

    def __repr__(self) -> str:
        return f'<PrintInstruction value={self.__value}>'
