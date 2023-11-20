from typing import List
from game.data.interfaces.users_repository_interface import UsersRepositoryInterface
from game.domain.models.users import Users

class UsersRepositoryMock(UsersRepositoryInterface):

    @classmethod
    def insert_user(cls, user_name: str, user_nickname: str, user_class_id: int, user_role: int) -> None:
        pass
            
    @classmethod
    def get_all_users(cls) -> List[Users]:
        return [Users(1, "Daniel", "dramos93", 1, 1)]
            
    @classmethod
    def get_user_by_id(cls, user_id: int) -> Users:
        return Users(1, "Daniel", "dramos93", 1, 1)

    @classmethod
    def nick_name_exists(cls, user_nick_name: str) -> bool:
        return True if user_nick_name == "dramos93" else False

    