# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring


from typing import Dict
from src.instruction.instruction import Instruction


class GotoInstruction(Instruction):
    def __init__(self, to: str) -> None:
        super().__init__()
        self.__to = to

    def get_goto(self, goto_dict: Dict[str, int]):
        return goto_dict.get(self.__to)

    def __repr__(self) -> str:
        return f'<GotoInstruction to={self.__to}>'
