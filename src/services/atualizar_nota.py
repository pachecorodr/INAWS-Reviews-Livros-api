from fastapi import HTTPException
from src.interfaces.models.livro_repository_interface import LivroRepositoryInterface
from src.interfaces.services.atualizar_nota_livro_interface import AtualizarNotaLivroInterface

class AtualizarNotaLivro(AtualizarNotaLivroInterface):
    """Classe de serviço para atualizar a nota de um livro."""

    def __init__(self, livro_repository: LivroRepositoryInterface):
        self.__livro_repository = livro_repository

    def atualizar(self, id: int, nota: int) -> dict:
        self.__validar_dados(nota)
        self.__atualizar_no_db(id, nota)
        return self.__formatar_resposta(id, nota)

    def __validar_dados(self, nota: int) -> None:
        
        if nota is None:
            raise HTTPException(status_code=422, detail="O campo 'nota' é obrigatório")

        if not isinstance(nota, int):
            raise HTTPException(status_code=422, detail="A nota precisa ser um inteiro")

        if not (0 <= nota <= 5):
            raise HTTPException(status_code=422, detail="A nota precisa estar entre 0 e 5")

    def __atualizar_no_db(self, id: int, nota: int) -> None:
        try:
            livro = self.__livro_repository.get_by_id(id)
            if not livro:
                raise HTTPException(status_code=404, detail="Livro não encontrado.")
            self.__livro_repository.update(id=id, nota=nota)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def __formatar_resposta(self, id: int, nota: int) -> dict:
        return {
            "data": {
                "type": "livro",
                "id": id,
                "attributes": {
                    "nota": nota
                }
            }
        }
