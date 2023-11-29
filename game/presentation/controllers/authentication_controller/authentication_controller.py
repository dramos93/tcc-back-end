from game.presentation.http_types.http_request import HttpRequest
from game.domain.user_cases.authentication.authentication_interface import (
    AuthenticationUserCaseInterface,
)
from game.presentation.http_types.http_response import HttpResponse
from game.presentation.interfaces.authentication_controller_interface import (
    AuthenticationControllerInterface,
)


class AuthenticationController(AuthenticationControllerInterface):
    def __init__(self, use_case: AuthenticationUserCaseInterface) -> None:
        self.__use_case = use_case

    def create_token(self, http_request: HttpRequest) -> HttpResponse:
        user_id = http_request.query_params["user_id"]
        body = self.__use_case.create_token(user_id=user_id)
        response = HttpResponse(body=body, status_code=200)

        return response

    def get_token(self, http_request: HttpRequest) -> HttpResponse:
        user_id = http_request.query_params["user_id"]
        body = self.__use_case.get_token(user_id=user_id)
        response = HttpResponse(body=body, status_code=200)

        return response

    def logout(self, http_request: HttpRequest) -> HttpResponse:
        user_id = http_request.query_params["user_id"]
        token = http_request.query_params["token"]
        body = self.__use_case.logout(user_id=user_id, token=token)
        response = HttpResponse(body=body, status_code=200)

        return response
