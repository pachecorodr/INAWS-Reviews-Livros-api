from fastapi import HTTPException
from src.interfaces.models.livro_repository_interface import LivroRepositoryInterface
from src.interfaces.services.criar_livro_interface import CriarLivroInterface

class CriarLivro(CriarLivroInterface):
    """Classe de serviço para criar um livro."""

    def __init__(self, livro_repository: LivroRepositoryInterface):
        self.__livro_repository = livro_repository

    def criar(self, dto: dict) -> dict:
        self.__validar_dados(dto)

        dto["titulo"] = dto["titulo"].strip()
        dto["descricao"] = dto["descricao"].strip()
        dto["imagem"] = dto["imagem"].strip()

        self.__criar_no_db(dto)

        return self.__formatar_resposta(dto)

    def __validar_dados(self, dto: dict) -> None:
        if not isinstance(dto, dict):
            raise HTTPException(status_code=422, detail="O DTO precisa ser um dicionário")

        required_fields = ["titulo", "descricao", "imagem"]
        for field in required_fields:
            if field not in dto or not dto[field]:
                raise HTTPException(status_code=422, detail=f"O campo '{field}' é obrigatório e não pode estar vazio.")

        if not isinstance(dto.get("titulo"), str):
            raise HTTPException(status_code=422, detail="O título precisa ser uma string")

        if not isinstance(dto.get("descricao"), str):
            raise HTTPException(status_code=422, detail="A descrição precisa ser uma string")

        if not isinstance(dto.get("imagem"), str):
            raise HTTPException(status_code=422, detail="A imagem precisa ser uma string")

    def __criar_no_db(self, dto: dict) -> None:
        """Insere o livro no banco de dados."""
        try:
            self.__livro_repository.create(dto)
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def __formatar_resposta(self, dto: dict) -> dict:
        return {
            "data": {
                "type": "livro",
                "count": 1,
                "attributes": dto
            }
        }
