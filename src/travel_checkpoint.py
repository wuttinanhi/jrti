# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring


from typing import List


class Checkpoint:
    def __init__(self, index: int) -> None:
        self.__index = index

    def get_index(self):
        return self.__index


class FunctionCheckpoint(Checkpoint):
    def __init__(self, current_pointer: int, store_key: str) -> None:
        super().__init__(current_pointer)
        self.__store_key = store_key

    def get_store_key(self):
        return self.__store_key


class TravelCheckPoint:
    def __init__(self) -> None:
        self.__data: List[Checkpoint] = []

    def push_checkpoint(self, checkpoint: Checkpoint):
        self.__data.append(checkpoint)

    def pop_checkpoint(self):
        return self.__data.pop()
