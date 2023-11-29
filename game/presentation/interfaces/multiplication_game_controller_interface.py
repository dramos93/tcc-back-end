from abc import ABC, abstractmethod
from game.presentation.http_types.http_request import HttpRequest
from game.presentation.http_types.http_response import HttpResponse


class MultiplicationGameControllerInterface(ABC):
    @abstractmethod
    def create_multiplication_game(self, http_request: HttpRequest) -> HttpResponse:
        pass

    @abstractmethod
    def get_all_multiplication_game(self, http_request: HttpRequest) -> HttpResponse:
        pass
