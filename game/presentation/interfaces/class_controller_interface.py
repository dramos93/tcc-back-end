from abc import ABC, abstractmethod
from game.presentation.http_types.http_request import HttpRequest
from game.presentation.http_types.http_response import HttpResponse


class MultiplicationGameControllerInterface(ABC):
    @abstractmethod
    def get_class(self, http_request: HttpRequest) -> HttpResponse:
        pass
