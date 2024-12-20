from game.presentation.http_types.http_request import HttpRequest
from game.domain.use_cases.user.user_interface import UserInterface
from game.presentation.http_types.http_response import HttpResponse
from game.presentation.interfaces.user_controller_interface import (
    UserControllerInterface,
)
from game.domain.use_cases.authentication.authentication_interface import (
    AuthenticationUserCaseInterface,
)


class UserController(UserControllerInterface):
    def __init__(
        self, use_case: UserInterface, auth_use_case: AuthenticationUserCaseInterface
    ) -> None:
        self.__use_case = use_case
        self.auth = auth_use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        token = http_request.headers.get("token")
        auth = self.is_auth(token, [1, 2, 3, 4])
        if auth:
            return auth
        user_id = http_request.query_params["user_id"]
        body = self.__use_case.find(user_id)
        response = HttpResponse(body=body, status_code=200)

        return response

    def create(self, http_request: HttpRequest) -> HttpResponse:
        # http_request = HttpRequest(**http_request)
        token = http_request.headers.get("token")
        auth = self.is_auth(token, [1, 2, 3, 4])
        if auth:
            return auth
        user_name = http_request.body["user_name"]
        user_nickname = http_request.body["user_nickname"]
        user_role = http_request.body["user_role"]
        user_password = http_request.body["user_password"]
        body = self.__use_case.register(
            user_name=user_name,
            user_nickname=user_nickname,
            user_role=user_role,
            user_password=user_password,
        )
        response = HttpResponse(body=body, status_code=200)

        return response

    def is_auth(self, token, roles_permission):
        user_permission = self.auth.get_user_permissions(token)
        if not user_permission:
            return HttpResponse(body={"message": "Não autorizado"}, status_code=401)
        if user_permission.get("user_role") not in roles_permission:
            return HttpResponse(body={"message": "Não autorizado"}, status_code=401)
