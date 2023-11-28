from typing import Dict
from game.data.interfaces.users_repository_interface import UsersRepositoryInterface
from game.domain.models.users import Users
from game.domain.user_cases.user_finder_interface import UserFinderInterface


class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def find(self, user_id: int) -> Dict:
        user = self.__search_user(user_id)
        response = self.__format__response(user)

        return response

    def __search_user(self, user_id: int) -> Users:
        user = self.__users_repository.get_user_by_id(user_id=user_id)
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
