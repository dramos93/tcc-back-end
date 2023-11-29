from game.presentation.http_types.http_request import HttpRequest
from game.domain.use_cases.user.user_interface import UserInterface
from game.presentation.http_types.http_response import HttpResponse
from game.presentation.interfaces.user_controller_interface import (
    UserControllerInterface,
)


class CreateUserController(UserControllerInterface):
    def __init__(self, use_case: UserInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        user_id = http_request.query_params["user_id"]
        body = self.__use_case.find(user_id)
        response = HttpResponse(body=body, status_code=200)

        return response

    def create(self, http_request: HttpRequest) -> HttpResponse:
        user_name = http_request.query_params["user_name"]
        user_nickname = http_request.query_params["user_nickname"]
        user_class_id = http_request.query_params["user_class_id"]
        user_role = http_request.query_params["user_role"]
        body = self.__use_case.register(
            user_name=user_name,
            user_nickname=user_nickname,
            user_class_id=user_class_id,
            user_role=user_role,
        )
        response = HttpResponse(body=body, status_code=200)

        return response
