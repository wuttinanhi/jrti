# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring


from typing import Dict
from src.instruction.instruction import Instruction


class CallFunctionInstruction(Instruction):
    def __init__(self, function_name: str, store_key: str) -> None:
        super().__init__()
        self.__function_name = function_name
        self.__store_key = store_key

    def get_function_name(self):
        return self.__function_name

    def get_store_key(self):
        return self.__store_key

    def get_goto(self, goto_dict: Dict[str, int]):
        return goto_dict.get(self.__function_name)

    def __repr__(self) -> str:
        return f'<CallFunctionInstruction name={self.__function_name} store={self.__store_key}>'
