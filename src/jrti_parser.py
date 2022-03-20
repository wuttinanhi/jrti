# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,invalid-name

import re
from typing import List


from src.instruction.block_instruction import BlockInstruction
from src.instruction.goto_instruction import GotoInstruction
from src.instruction.if_instruction import IfInstruction
from src.instruction.instruction import Instruction
from src.instruction.math_instruction import MathInstruction
from src.instruction.print_instruction import PrintInstruction
from src.instruction.print_line_instruction import PrintLineInstruction
from src.instruction.recieve_input_instruction import RecieveInputInstruction
from src.instruction.set_instruction import SetInstruction
from src.value import Value


class Parser:
    def __init__(self, script_path: str) -> None:
        self.__script_path = script_path
        self.__scripts: List[str] = []
        self.__instructions: List[Instruction] = []
        self.__goto_dict = {}

    def __openfile(self, path: str):
        with open(path, mode="r", encoding="utf-8") as file:
            self.__scripts = file.read().splitlines()
        return self.__scripts

    def get_instruction(self):
        return self.__instructions

    def get_goto_dict(self):
        return self.__goto_dict

    def parse(self):
        self.__openfile(self.__script_path)

        for line in self.__scripts:
            # if comment skip
            if line.startswith("#"):
                continue

            # splitter
            split = line.split(" ")
            keyword = split[0]

            # print instruction
            if keyword == "PRINT":
                self.add_print_instruction(line)

            # set instruction
            if keyword == "SET":
                self.add_set_instruction(line)

            # input instruction
            if keyword == "INPUT":
                self.add_input_instruction(line)

            # math instruction
            if keyword == "MATH":
                self.add_math_instruction(line)

            # block instruction
            if keyword == "BLOCK":
                self.add_block_instruction(line)

            # goto instruction
            if keyword == "GOTO":
                self.add_goto_instruction(line)

            # if instruction
            if keyword == "IF":
                self.add_if_instruction(line)

            # print line instruction
            if keyword == "PRINTLN":
                self.add_print_line_instruction(line)

        return self.__instructions

    def add_print_instruction(self, line: str):
        value = Value(line[6:])
        instruction = PrintInstruction(value)
        self.__instructions.append(instruction)

    def add_set_instruction(self, line: str):
        key = line.split(" ")[1]
        value = Value(line.split(" = ")[1])
        instruction = SetInstruction(key, value)
        self.__instructions.append(instruction)

    def add_input_instruction(self, line: str):
        key = line.split(" ")[1]
        instruction = RecieveInputInstruction(key)
        self.__instructions.append(instruction)

    def add_math_instruction(self, line: str):
        key = line.split(" ")[1]
        operator = line.split(" ")[2]
        value = Value(line.split(" ")[3])
        instruction = MathInstruction(key, operator, value)
        self.__instructions.append(instruction)

    def add_block_instruction(self, line: str):
        name = line.split(" ")[1]
        instruction = BlockInstruction(name)
        self.__instructions.append(instruction)
        self.__goto_dict[name] = len(self.__instructions) - 1

    def add_goto_instruction(self, line: str):
        goto_name = line.split(" ")[1]
        instruction = GotoInstruction(goto_name)
        self.__instructions.append(instruction)

    def add_if_instruction(self, line: str):
        # IF $condition == 1 GOTO true

        regex = re.split(r'(IF)\s(.+)\s(\W\W|\W)\s(.+)\sGOTO\s(.+)', line)

        a: Value = Value(regex[2])
        compare: str = regex[3]
        b: Value = Value(regex[4])
        if_true_goto: str = regex[5]

        instruction = IfInstruction(a, compare, b, if_true_goto)
        self.__instructions.append(instruction)

    def add_print_line_instruction(self, line: str):
        value = Value(line[8:])
        instruction = PrintLineInstruction(value)
        self.__instructions.append(instruction)
