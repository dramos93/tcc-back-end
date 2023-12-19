from game.data import use_cases
from game.domain.use_cases.classes.class_interface import ClassesUseCaseInterface
from game.presentation.http_types.http_request import HttpRequest
from game.presentation.http_types.http_response import HttpResponse
from game.presentation.interfaces import class_controller_interface


class ClassesController(class_controller_interface):
    def __init__(self, use_case: ClassesUseCaseInterface) -> None:
        self.use_Case = use_case

    def get_class(http_request: HttpRequest) -> HttpResponse:
        user_id = http_request.path_params["user_id"]
        body = use_cases.get_class(user_id=user_id)
        response = HttpResponse(body=body, status_code=200)
        return response
