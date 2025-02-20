from src.interfaces.controllers.controllers_interface import ControllerInterface
from src.interfaces.services.criar_livro_interface import CriarLivroInterface
from src.controllers.http_types.http_request import HttpRequest
from src.controllers.http_types.http_response import HttpResponse

class CriarLivroController(ControllerInterface):
    """Classe de controller para criar um livro."""

    def __init__(self, criar_livro_service: CriarLivroInterface):
        self.__criar_livro_service = criar_livro_service

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        dto = http_request.body
        body_response = self.__criar_livro_service.criar(dto)

        return HttpResponse(status_code=201, body=body_response)
