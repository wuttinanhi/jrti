# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring


from src.instruction.instruction import Instruction
from src.value import Value
from src.travel_checkpoint import FunctionCheckpoint


class ReturnInstruction(Instruction):
    def __init__(self, return_value: Value) -> None:
        super().__init__()
        self.__return_value = return_value

    def get_goto(self, checkpoint: FunctionCheckpoint):
        return checkpoint.get_index() + 1

    def get_result(self):
        return self.__return_value.get(self.get_variable_storage())

    def __repr__(self) -> str:
        return f'<ReturnInstruction value={self.__return_value}>'
