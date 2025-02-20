from src.interfaces.controllers.controllers_interface import ControllerInterface
from src.interfaces.services.atualizar_nota_livro_interface import AtualizarNotaLivroInterface
from src.controllers.http_types.http_request import HttpRequest
from src.controllers.http_types.http_response import HttpResponse

class AtualizarNotaLivroController(ControllerInterface):
    """Classe de controller para atualizar a nota de um livro."""

    def __init__(self, atualizar_nota_livro_service: AtualizarNotaLivroInterface):
        self.__atualizar_nota_livro_service = atualizar_nota_livro_service

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        id = http_request.param.get('id')
        nota = http_request.param.get('nota')

        body_response = self.__atualizar_nota_livro_service.atualizar(id, nota)

        return HttpResponse(status_code=200, body=body_response)
