from src.interfaces.models.db_connection_interface import DBConnectionInterface
from src.interfaces.models.livro_repository_interface import LivroRepositoryInterface
from src.models.entities.livro import LivroTable


class LivroRepository(LivroRepositoryInterface):
    """Classe que representa o repositório de livros."""
    
    def __init__(self, db_connection: DBConnectionInterface):
        self.__db_connection = db_connection

    def create(self, dto: dict) -> None:
        with self.__db_connection as database:
            try:
                data_obj = LivroTable(
                    titulo=dto.get("titulo"),
                    descricao=dto.get("descricao"),
                    imagem=dto.get("imagem")
                )
                database.session.add(data_obj)
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e
            
    def get_all(self) -> list[LivroTable]:
        with self.__db_connection as database:
            try:
                return database.session.query(LivroTable).all()
            except Exception as e:
                raise e
            
    def get_by_id(self, id: int) -> LivroTable:
        with self.__db_connection as database:
            try:
                return database.session.query(LivroTable).filter(LivroTable.id == id).first()
            except Exception as e:
                raise e

    def update(self, nota: int, id: int) -> None:
        with self.__db_connection as database:
            try:
                database.session.query(LivroTable).filter(LivroTable.id == id).update({LivroTable.nota: nota})
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e

    def delete(self, id: int) -> None:
        with self.__db_connection as database:
            try:
                database.session.query(LivroTable).filter(LivroTable.id == id).delete()
                database.session.commit()
            except Exception as e:
                database.session.rollback()
                raise e
