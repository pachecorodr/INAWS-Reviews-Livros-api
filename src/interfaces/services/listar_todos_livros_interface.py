from abc import ABC, abstractmethod

class ListarTodosLivrosInterface(ABC):

    @abstractmethod
    def listar(self) -> dict:
        pass
