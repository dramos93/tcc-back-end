from game.presentation.http_types.http_request import HttpRequest
from game.domain.use_cases.authentication.authentication_interface import (
    AuthenticationUserCaseInterface,
)
from game.presentation.http_types.http_response import HttpResponse
from game.presentation.interfaces.authentication_controller_interface import (
    AuthenticationControllerInterface,
)


class AuthenticationController(AuthenticationControllerInterface):
    def __init__(self, use_case: AuthenticationUserCaseInterface, auth_use_case: AuthenticationUserCaseInterface) -> None:
        self.__use_case = use_case
        self.auth = auth_use_case

    def create_token(self, http_request: HttpRequest) -> HttpResponse:
        token = http_request.headers.get("token")
        auth = self.is_auth(token, [1, 2, 3, 4])
        if auth:
            return auth
        user_id = http_request.body["user_id"]
        user_password = http_request.body["user_password"]
        body = self.__use_case.create_token(
            user_id=user_id, user_password=user_password
        )
        response = HttpResponse(body=body, status_code=200)
        return response

    def get_token(self, http_request: HttpRequest) -> HttpResponse:
        token = http_request.headers.get("token")
        auth = self.is_auth(token, [1, 2, 3, 4])
        if auth:
            return auth
        token = http_request.headers["token"]
        body = self.__use_case.get_user_permissions(token)
        response = HttpResponse(body=body, status_code=200)
        return response

    def logout(self, http_request: HttpRequest) -> HttpResponse:
        token = http_request.headers.get("token")
        auth = self.is_auth(token, [1, 2, 3, 4])
        if auth:
            return auth
        user_id = http_request.body["user_id"]
        token = http_request.body["token"]
        body = self.__use_case.logout(user_id=user_id, token=token)
        response = HttpResponse(body=body, status_code=200)
        return response
    
    def is_auth(self, token, roles_permission):
        user_permission = self.auth.get_user_permissions(token)
        if not user_permission:
            return HttpResponse(body={"message": "Não autorizado"}, status_code=401)
        if user_permission.get("user_role") not in roles_permission:
            return HttpResponse(body={"message": "Não autorizado"}, status_code=401)
