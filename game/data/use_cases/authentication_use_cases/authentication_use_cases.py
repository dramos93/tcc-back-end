from typing import Dict
from uuid import UUID
from game.data.interfaces.authentication_repository_interface import (
    AuthenticationRepositoryInterface,
)
from game.data.interfaces.users_repository_interface import UsersRepositoryInterface
from game.domain.models.authentication_model import AuthenticationModel
from game.domain.use_cases.authentication.authentication_interface import (
    AuthenticationUserCaseInterface,
)


class AuthenticationUseCases(AuthenticationUserCaseInterface):
    def __init__(
        self,
        authentication_repository: AuthenticationRepositoryInterface,
        user_repository: UsersRepositoryInterface,
    ) -> None:
        self.authentication_repository = authentication_repository
        self.user_repository = user_repository

    def create_token(self, user_id: int) -> None:
        self.__user_exists(user_id=user_id)
        self.authentication_repository.create(user_id)

    def get_token(self, user_id: int) -> Dict:
        self.__user_exists(user_id=user_id)
        authentication_repository = self.authentication_repository.get_token(
            user_id=user_id
        )

        return self.__ajust_response(authentication_repository)

    def logout(self, user_id: int, token: UUID) -> None:
        self.__user_exists(user_id=user_id)
        self.authentication_repository.logout(user_id=user_id, token=token)

    @classmethod
    def __ajust_response(cls, authentication: AuthenticationModel) -> Dict:
        response = {
            "user_id": authentication.user_id,
            "token": authentication.token,
            "created_on": authentication.created_on,
            "active": authentication.active,
        }

        return response

    def __user_exists(self, user_id: int) -> bool:
        if self.user_repository.get_user_by_id(user_id=user_id) is None:
            raise Exception("Usuário não encontrado.")
        return True
