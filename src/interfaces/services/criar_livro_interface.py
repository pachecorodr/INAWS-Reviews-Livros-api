from abc import ABC, abstractmethod

class CriarLivroInterface (ABC):
    
    @abstractmethod
    def criar(self, dto: dict) -> dict:
        pass
