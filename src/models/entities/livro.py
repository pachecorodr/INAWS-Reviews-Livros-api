from sqlalchemy import Column, Integer, String
from src.models.base import Base

class LivroTable(Base):
    __tablename__ = "livros"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    titulo = Column(String(255), nullable=False)
    descricao = Column(String(255), nullable=False)
    imagem = Column(String(255), nullable=False)
    nota = Column (Integer, nullable=True)
