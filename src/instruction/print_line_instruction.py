# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring


from src.instruction.instruction import Instruction
from src.value import Value


class PrintLineInstruction(Instruction):
    def __init__(self, value: Value) -> None:
        super().__init__()
        self.__value = value

    def run(self):
        text = self.__value.get(self.get_variable_storage())
        print(text)

    def __repr__(self) -> str:
        return f'<PrintLineInstruction value={self.__value}>'
