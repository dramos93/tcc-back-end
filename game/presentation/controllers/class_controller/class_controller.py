from game.domain.use_cases.classes.class_interface import ClassesUseCaseInterface
from game.presentation.interfaces.class_controller_interface import (
    ClassesControllerInterface,
)
from game.presentation.http_types.http_request import HttpRequest
from game.presentation.http_types.http_response import HttpResponse


class ClassesController(ClassesControllerInterface):
    def __init__(self, use_case: ClassesUseCaseInterface) -> None:
        self.__use_Case = use_case

    def get_class(self, http_request: HttpRequest) -> HttpResponse:
        user_id = http_request.query_params["user_id"]
        body = self.__use_Case.get_class(user_id=user_id)
        response = HttpResponse(body=body, status_code=200)
        return response
