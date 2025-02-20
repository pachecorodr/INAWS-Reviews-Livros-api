from fastapi import HTTPException
from src.interfaces.models.livro_repository_interface import LivroRepositoryInterface
from src.interfaces.services.listar_todos_livros_interface import ListarTodosLivrosInterface
from src.models.entities.livro import LivroTable

class ListarTodosLivros(ListarTodosLivrosInterface):
    """Classe de serviço para listar todos os livros."""

    def __init__(self, livro_repository: LivroRepositoryInterface):
        self.__livro_repository = livro_repository

    def listar(self) -> dict:
        return self.__formatar_resposta(self.__listar_do_db())

    def __listar_do_db(self) -> list[LivroTable]:
        try:
            return self.__livro_repository.get_all()
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def __formatar_resposta(self, livros: list[LivroTable]) -> dict:
        lista_formatada = []

        for livro in livros:
            lista_formatada.append({
                "id": livro.id,
                "titulo": livro.titulo,
                "descricao": livro.descricao,
                "imagem": livro.imagem,
                "nota": livro.nota
            })

        return {
            "data": {
                "type": "livro",
                "count": len(lista_formatada),
                "attributes": lista_formatada
            }
        }
