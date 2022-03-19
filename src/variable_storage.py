# pylint: disable=missing-module-docstring,missing-class-docstring,missing-function-docstring


class VariableStorage:
    def __init__(self) -> None:
        self.__storage = {}

    def get(self, key: str):
        return self.__storage.get(key)

    def set(self, key: str, value: any):
        self.__storage[key] = value
