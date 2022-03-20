# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,unused-private-member


from src.instruction.instruction import Instruction
from src.value import Value


class RecieveInputInstruction(Instruction):
    def __init__(self, key: str) -> None:
        super().__init__()
        self.__key = key

    def run(self):
        variable_storage = self.get_variable_storage()
        receive_input = input()
        value = Value(receive_input)
        variable_storage.set(self.__key, value.get(self.get_variable_storage))

    def __repr__(self) -> str:
        return f'<RecieveInputInstruction key={self.__key}>'
