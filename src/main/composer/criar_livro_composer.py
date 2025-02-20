from src.models.settings.db_conn_handler import postgres_connection_handler
from src.models.repositories.livro_repository import LivroRepository
from src.services.criar_livro import CriarLivro
from src.controllers.criar_livro_controller import CriarLivroController

def criar_livro_composer () -> CriarLivroController:
    model = LivroRepository(postgres_connection_handler)
    service = CriarLivro(model)
    controller = CriarLivroController(service)
    return controller
