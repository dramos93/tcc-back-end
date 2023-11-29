from abc import ABC, abstractmethod
from game.presentation.http_types.http_request import HttpRequest
from game.presentation.http_types.http_response import HttpResponse


class AuthenticationControllerInterface(ABC):
    @abstractmethod
    def create_token(self, http_request: HttpRequest) -> None:
        pass

    @abstractmethod
    def get_token(self, http_request: HttpRequest) -> HttpResponse:
        pass

    @abstractmethod
    def logout(self, http_request: HttpRequest) -> None:
        pass
