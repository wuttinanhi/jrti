# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring

from ast import List

from src.instruction.goto_instruction import GotoInstruction
from src.instruction.if_instruction import IfInstruction
from src.instruction.instruction import Instruction
from src.instruction.return_instruction import ReturnInstruction
from src.jrti_parser import Parser
from src.travel_checkpoint import FunctionCheckpoint, TravelCheckPoint
from src.variable_storage import VariableStorage
from src.instruction.call_function_instruction import CallFunctionInstruction


class JRTI:
    def __init__(self) -> None:
        self.__instructions: List[Instruction] = []
        self.__goto_dict = {}
        self.__travel_checkpoint = TravelCheckPoint()

        # set predefine variable
        self.__variable_storage: VariableStorage = VariableStorage()
        self.__variable_storage.set("$__NEWLINE", '\n')

    def get_goto_dict(self):
        return self.__goto_dict

    def get_travel_checkpoint(self):
        return self.__travel_checkpoint

    def get_variable_storage(self):
        return self.__variable_storage

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
            current_instruction.set_variable_storage(
                self.get_variable_storage()
            )

            if (
                isinstance(current_instruction, IfInstruction) or
                isinstance(current_instruction, GotoInstruction)
            ):
                goto = current_instruction.get_goto(self.get_goto_dict())
                if goto is not None:
                    pointer = goto
                    continue

            if isinstance(current_instruction, CallFunctionInstruction):
                store_key = current_instruction.get_store_key()
                checkpoint = FunctionCheckpoint(pointer, store_key)
                self.get_travel_checkpoint().push_checkpoint(checkpoint)

                goto = current_instruction.get_goto(self.get_goto_dict())
                if goto is not None:
                    pointer = goto
                    continue

            if isinstance(current_instruction, ReturnInstruction):
                last_checkpoint: FunctionCheckpoint = self.get_travel_checkpoint().pop_checkpoint()

                store_key = last_checkpoint.get_store_key()
                result = current_instruction.get_result()
                self.get_variable_storage().set(store_key, result)

                goto = current_instruction.get_goto(last_checkpoint)
                if goto is not None:
                    pointer = goto
                    continue

            current_instruction.run()

            pointer += 1
