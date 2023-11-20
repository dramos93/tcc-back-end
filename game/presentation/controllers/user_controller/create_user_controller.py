from game.presentation.http_types.http_request import HttpRequest
from game.domain.user_cases.user_finder_interface import UserFinderInterface
from game.presentation.http_types.http_response import HttpResponse
from game.presentation.interfaces.user_controller_interface import UserControllerInterface



class CreateUserController(UserControllerInterface):
    def __init__(self, use_case: UserFinderInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        #  http_request
        user_id = http_request.query_params["user_id"]
        body = self.__use_case.find(user_id)
        response = HttpResponse(body=body, status_code=200)

        return response
         