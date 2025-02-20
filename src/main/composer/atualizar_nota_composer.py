from src.models.settings.db_conn_handler import postgres_connection_handler
from src.models.repositories.livro_repository import LivroRepository
from src.services.atualizar_nota import AtualizarNotaLivro
from src.controllers.atualizar_nota_controller import AtualizarNotaLivroController

def atualizar_nota_composer () -> AtualizarNotaLivroController:
    model = LivroRepository(postgres_connection_handler)
    service = AtualizarNotaLivro(model)
    controller = AtualizarNotaLivroController(service)
    return controller
