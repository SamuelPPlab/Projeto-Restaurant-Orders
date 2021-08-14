from abc import ABC, abstractmethod


class Handler(ABC):
    @staticmethod
    @abstractmethod
    def read(file_name: str):
        raise NotImplementedError

    @staticmethod
    @abstractmethod
    def writer(texts: list[str], file_name: str):
        raise NotImplementedError
