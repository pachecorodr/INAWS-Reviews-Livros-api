from src.models.settings.db_conn_handler import postgres_connection_handler
from src.models.repositories.livro_repository import LivroRepository
from src.services.deletar_livro import DeletarLivro
from src.controllers.deletar_livro_controller import DeletarLivroController

def deletar_livro_composer () -> DeletarLivroController:
    model = LivroRepository(postgres_connection_handler)
    service = DeletarLivro(model)
    controller = DeletarLivroController(service)
    return controller
