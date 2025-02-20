from abc import ABC, abstractmethod
from src.models.entities.livro import LivroTable

class LivroRepositoryInterface (ABC):
    
    @abstractmethod
    def create(self, dto: dict) -> None:
        pass
    
    @abstractmethod        
    def get_all(self) -> list[LivroTable]:
        pass
            
    @abstractmethod
    def update(self, nota: int, id: int) -> None:
        pass
    
    @abstractmethod
    def delete(self, id: int) -> None:
        pass
