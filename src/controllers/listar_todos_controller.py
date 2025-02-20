from src.interfaces.controllers.controllers_interface import ControllerInterface
from src.interfaces.services.listar_todos_livros_interface import ListarTodosLivrosInterface
from src.controllers.http_types.http_request import HttpRequest
from src.controllers.http_types.http_response import HttpResponse

class ListarTodosLivrosController(ControllerInterface):
    """Classe de controller para listar todos os livros."""

    def __init__(self, listar_todos_livros_service: ListarTodosLivrosInterface):
        self.__listar_todos_livros_service = listar_todos_livros_service

    def handle(self, request: HttpRequest) -> HttpResponse:
        """Recebe a requisição, processa e retorna a resposta."""

        body_response = self.__listar_todos_livros_service.listar()

        return HttpResponse(status_code=200, body=body_response)
