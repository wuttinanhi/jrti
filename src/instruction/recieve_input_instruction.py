# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,unused-private-member


from src.value import Value
from src.instruction.instruction import Instruction


class RecieveInputInstruction(Instruction):
    def __init__(self, key: str) -> None:
        super().__init__()
        self.__key = key

    def run(self):
        variable_storage = self.get_variable_storage()
        value = input()
        variable_storage.set(self.__key, value)

    def __repr__(self) -> str:
        return f'<RecieveInputInstruction key={self.__key}>'
