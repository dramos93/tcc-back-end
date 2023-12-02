from datetime import date
from uuid import UUID, uuid1, getnode
from game.data.interfaces.authentication_repository_interface import (
    AuthenticationRepositoryInterface,
)
from game.domain.models.authentication_model import AuthenticationModel


authentication_mock = {"token": uuid1(), "created_on": date.today(), "active": True}


class AuthenticationRepositoryMock(AuthenticationRepositoryInterface):
    @classmethod
    def create(cls, user_id: int) -> AuthenticationModel:
        authentication_model = AuthenticationModel(
            **authentication_mock, user_id=user_id
        )
        return authentication_model

    @classmethod
    def logout(cls, user_id: int, token: UUID) -> None:
        pass

    @classmethod
    def get_credentials_from_token(cls, token: UUID) -> AuthenticationModel:
        authentication_model = AuthenticationModel(**authentication_mock, user_id=1)
        return authentication_model
