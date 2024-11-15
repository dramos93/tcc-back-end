from game.domain.use_cases.authentication.authentication_interface import (
    AuthenticationUserCaseInterface,
)
from game.domain.use_cases.classes.class_interface import ClassesUseCaseInterface
from game.presentation.interfaces.class_controller_interface import (
    ClassesControllerInterface,
)
from game.presentation.http_types.http_request import HttpRequest
from game.presentation.http_types.http_response import HttpResponse


class ClassesController(ClassesControllerInterface):
    def __init__(
        self,
        use_case: ClassesUseCaseInterface,
        auth_use_case: AuthenticationUserCaseInterface,
    ) -> None:
        self.__use_Case = use_case
        self.auth = auth_use_case

    def get_class(self, http_request: HttpRequest) -> HttpResponse:
        token = http_request.headers.get("token")
        auth = self.is_auth(token, [1, 2, 3, 4])
        if auth:
            return auth
        user_id = http_request.query_params["user_id"]
        body = self.__use_Case.get_class(user_id=user_id)
        response = HttpResponse(body=body, status_code=200)
        return response
    
    def get_classes(self, http_request: HttpRequest) -> HttpResponse:
        token = http_request.headers.get("token")
        auth = self.is_auth(token, [1, 2, 3, 4])
        if auth:
            return auth
        body = self.__use_Case.get_classes()
        response = HttpResponse(body=body, status_code=200)
        return response


    def is_auth(self, token, roles_permission):
        if not token or token == '':
            return HttpResponse(body={"message": "token vazio ou nulo."}, status_code=401)
        user_permission = self.auth.get_user_permissions(token)
        if not user_permission:
            return HttpResponse(body={"message": "Não autorizado"}, status_code=401)
        if user_permission.get("user_role") not in roles_permission:
            return HttpResponse(body={"message": "Não autorizado"}, status_code=401)
