# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring


from src.instruction.instruction import Instruction
from src.value import Value


class SetInstruction(Instruction):
    def __init__(self, key: str, value: Value) -> None:
        super().__init__()
        self.__key = key
        self.__value = value

    def run(self):
        variable_storage = self.get_variable_storage()
        variable_storage.set(self.__key, self.__value)

    def __repr__(self) -> str:
        return f'<SetInstruction key={self.__key} value={self.__value}>'
