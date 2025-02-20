from src.interfaces.controllers.controllers_interface import ControllerInterface
from src.interfaces.services.deletar_livro_interface import DeletarLivroInterface
from src.controllers.http_types.http_request import HttpRequest
from src.controllers.http_types.http_response import HttpResponse

class DeletarLivroController(ControllerInterface):
    """Classe de controller para deletar um livro."""

    def __init__(self, deletar_livro_service: DeletarLivroInterface):
        self.__deletar_livro_service = deletar_livro_service

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        id = http_request.param.get("id")
        self.__deletar_livro_service.deletar(id)

        return HttpResponse(status_code=204, body=None)
