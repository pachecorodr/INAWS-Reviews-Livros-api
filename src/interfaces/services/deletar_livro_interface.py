from abc import ABC, abstractmethod

class DeletarLivroInterface(ABC):
    
    @abstractmethod
    def deletar(self, id: int) -> None:
        pass
