from fastapi import HTTPException
from src.interfaces.models.livro_repository_interface import LivroRepositoryInterface
from src.interfaces.services.deletar_livro_interface import DeletarLivroInterface

class DeletarLivro(DeletarLivroInterface):
    """Classe para deletar um livro."""

    def __init__(self, livro_repository: LivroRepositoryInterface):
        self.__livro_repository = livro_repository

    def deletar(self, id: int) -> None:
        self.__deletar_no_db(id)    

    def __deletar_no_db(self, id: int) -> None:
        try:
            livro = self.__livro_repository.get_by_id(id)
            if not livro:
                raise HTTPException(status_code=404, detail="Livro não encontrado.")
            self.__livro_repository.delete(id)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
