from abc import ABC, abstractmethod

class AtualizarNotaLivroInterface(ABC):
    
    @abstractmethod
    def atualizar(self, id: int, nota: int) -> dict:
        pass
