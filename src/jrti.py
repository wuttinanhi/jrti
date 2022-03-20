# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

from ast import List
from src.instruction.goto_instruction import GotoInstruction
from src.instruction.if_instruction import IfInstruction
from src.instruction.instruction import Instruction
from src.jrti_parser import Parser
from src.variable_storage import VariableStorage


class JRTI:
    def __init__(self) -> None:
        self.__instructions: List[Instruction] = []
        self.__goto_dict = {}

        # set predefine variable
        self.__variable_storage: VariableStorage = VariableStorage()
        self.__variable_storage.set("$__NEWLINE", '\n')

    def run(self, script_path: str):
        parser = Parser(script_path)
        parser.parse()
        self.__instructions = parser.get_instruction()
        self.__goto_dict = parser.get_goto_dict()
        pointer = 0

        while True:
            if pointer >= len(self.__instructions):
                break

            current_instruction = self.__instructions[pointer]
            current_instruction.set_variable_storage(self.__variable_storage)

            if (
                isinstance(current_instruction, IfInstruction) or
                isinstance(current_instruction, GotoInstruction)
            ):
                goto = current_instruction.get_goto(self.__goto_dict)
                if goto is not None:
                    pointer = goto
                    continue

            current_instruction.run()

            pointer += 1
