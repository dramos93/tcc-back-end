from abc import ABC, abstractmethod
from game.presentation.http_types.http_request import HttpRequest
from game.presentation.http_types.http_response import HttpResponse

class UserControllerInterface(ABC):
    
    @abstractmethod
    def handle(self, http_request: HttpRequest) -> HttpResponse : pass