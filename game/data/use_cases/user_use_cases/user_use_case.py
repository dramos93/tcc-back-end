from typing import Dict
from game.data.interfaces.users_repository_interface import UsersRepositoryInterface
from game.domain.models.users import Users
from game.domain.use_cases.user.user_interface import UserInterface


class UserUseCase(UserInterface):
    def __init__(
        self,
        user_use_case: UsersRepositoryInterface,
    ) -> None:
        self.__user_repository = user_use_case

    def find(self, user_id: int) -> Dict:
        user = self.__search_user(user_id=user_id)
        response = self.__format__response(user=user)

        return response

    def register(
        self,
        user_name: str,
        user_nickname: str,
        user_role: int,
        user_password: str,
    ) -> None:
        # Validar se o nickname já existe
        self.__user_nickname_exists(user_nickname=user_nickname)

        # Validar a string
        self.__validate_name(name=user_name)

        self.__user_repository.insert_user(
            user_name=user_name,
            user_nickname=user_nickname,
            user_role=user_role,
            user_password=user_password,
        )

    def __user_nickname_exists(self, user_nickname: str) -> None:
        if self.__user_repository.nick_name_exists(user_nickname):
            raise Exception("O username já existe.")

    @classmethod
    def __validate_name(cls, name: str) -> None:
        if not name.isalpha():
            raise Exception("Deve conter só letra.")

    def __search_user(self, user_id: int) -> Users:
        user = self.__user_repository.get_user_by_id(user_id=user_id)
        if user is None:
            raise Exception("Usuário não encontrado.")
        return user

    @classmethod
    def __format__response(cls, user: Users) -> Dict:
        response = {
            "user_id": user.user_id,
            "user_name": user.user_name,
            "user_nickname": user.user_nickname,
            "user_role": user.user_role,
        }
        return response
