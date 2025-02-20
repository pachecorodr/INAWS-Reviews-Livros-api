from src.models.settings.db_conn_handler import postgres_connection_handler
from src.models.repositories.livro_repository import LivroRepository
from src.services.listar_todos import ListarTodosLivros
from src.controllers.listar_todos_controller import ListarTodosLivrosController

def listar_todos_composer () -> ListarTodosLivrosController:
    model = LivroRepository(postgres_connection_handler)
    service = ListarTodosLivros(model)
    controller = ListarTodosLivrosController(service)
    return controller
