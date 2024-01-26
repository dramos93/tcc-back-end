from game.domain.use_cases.authentication.authentication_interface import AuthenticationUserCaseInterface
from game.presentation.http_types.http_request import HttpRequest
from game.domain.use_cases.multiplication_game.multiplication_game_interface import (
    MultiplicationGameInterface,
)
from game.presentation.http_types.http_response import HttpResponse
from game.presentation.interfaces.multiplication_game_controller_interface import (
    MultiplicationGameControllerInterface,
)


class MultiplicationGameController(MultiplicationGameControllerInterface):
    def __init__(self, use_case: MultiplicationGameInterface, auth_use_case: AuthenticationUserCaseInterface) -> None:
        self.__use_case = use_case
        self.auth = auth_use_case

    def create_multiplication_game(self, http_request: HttpRequest) -> HttpResponse:
        token = http_request.headers.get("token")
        auth = self.is_auth(token, [1, 2, 3, 4])
        if auth:
            return auth
        user_id = http_request.body["user_id"]
        class_id = http_request.body["class_id"]
        multiplication_table = http_request.body["multiplication_table"]
        round = http_request.body["round"]
        errors = http_request.body["errors"]
        body = self.__use_case.create_multiplication_game(
            user_id=user_id,
            class_id=class_id,
            multiplication_table=multiplication_table,
            round=round,
            errors=errors,
        )
        response = HttpResponse(body=body, status_code=200)
        return response

    def get_all_multiplication_game(self, http_request: HttpRequest) -> HttpResponse:
        token = http_request.headers.get("token")
        auth = self.is_auth(token, [1, 2, 3, 4])
        if auth:
            return auth
        user_id = http_request.query_params["user_id"]
        class_id = http_request.query_params["class_id"]
        body = self.__use_case.get_multiplication_game(
            user_id=user_id, class_id=class_id
        )
        response = HttpResponse(body=body, status_code=200)

        return response

    def is_auth(self, token, roles_permission):
        user_permission = self.auth.get_user_permissions(token)
        if not user_permission:
            return HttpResponse(body={"message": "Não autorizado"}, status_code=401)
        if user_permission.get("user_role") not in roles_permission:
            return HttpResponse(body={"message": "Não autorizado"}, status_code=401)