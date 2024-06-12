from typing import Dict
from uuid import UUID
from game.data.interfaces.authentication_repository_interface import (
    AuthenticationRepositoryInterface,
)
from game.data.interfaces.users_repository_interface import UsersRepositoryInterface
from game.domain.models.authentication_model import AuthenticationModel
from game.domain.models.users import Users
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

    def create_token(self, user_nickname: str, user_password: str) -> Dict:
        try:
            user_id = self.__logged(user_nickname=user_nickname, user_password=user_password)
            new_auth = self.authentication_repository.create(user_id)
            user = self.__user(new_auth.user_id)
        except Exception as e:
            raise(e)
        else:
            return self.__ajust_response(new_auth, user)

    def get_user_permissions(self, token: UUID | None) -> Dict | None:
        try:
            token = UUID(str(token))
        except ValueError:
            raise ValueError("Invalid token format.")
        # Add your validation logic here
        authentication_repository = (
            self.authentication_repository.get_credentials_from_token(token)
        )
        if not authentication_repository:
            return {}
        user = self.__user(authentication_repository.user_id)
        return self.__ajust_response(authentication_repository, user)

    def logout(self, user_id: int, token: UUID | None) -> None:
        try:
            token = UUID(str(token))
        except ValueError:
            raise ValueError("Invalid token format.")
        self.__user(user_id=user_id)
        self.authentication_repository.logout(user_id=user_id, token=token)

    @classmethod
    def __ajust_response(cls, authentication: AuthenticationModel, user: Users) -> Dict:
        response = {
            "user_id": authentication.user_id,
            "token": str(authentication.token),
            "created_on": str(authentication.created_on),
            "active": authentication.active,
            "user_name": user.user_name,
            "user_nickname": user.user_nickname,
            "user_role": user.user_role,
        }
        return response

    def __user(self, user_id: int) -> Users:
        user = self.user_repository.get_user_by_id(user_id=user_id)
        if user is None:
            raise Exception("Usuário não encontrado.")
        return user

    def __logged(self, user_nickname: str, user_password: str) -> int:
        login = self.user_repository.login(user_nickname=user_nickname, user_password=user_password)
        if not login:
            raise Exception("Usuário ou senha não existe.")
        return login.user_id