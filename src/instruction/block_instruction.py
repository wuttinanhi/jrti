# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring


from src.instruction.instruction import Instruction


class BlockInstruction(Instruction):
    def __init__(self, name: str) -> None:
        super().__init__()
        self.__name = name

    def get_name(self):
        return self.__name

    def __repr__(self) -> str:
        return f'<BlockInstruction name={self.__name}>'
