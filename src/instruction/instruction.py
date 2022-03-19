# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring,unused-private-member


from src.variable_storage import VariableStorage


class Instruction:
    def __init__(self) -> None:
        self.__variable_storage: VariableStorage = None

    def run(self):
        pass

    def set_variable_storage(self, storage: VariableStorage):
        self.__variable_storage = storage

    def get_variable_storage(self):
        return self.__variable_storage
