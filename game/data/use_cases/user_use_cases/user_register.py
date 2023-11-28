from game.data.interfaces.class_repository_interface import ClassRepositoryInterface
from game.data.interfaces.users_repository_interface import UsersRepositoryInterface
from game.domain.user_cases.user_register_interface import UserRegisterInterface


class UserRegisterUseCase(UserRegisterInterface):
    def __init__(
        self,
        user_use_case: UsersRepositoryInterface,
        class_user_case: ClassRepositoryInterface,
    ) -> None:
        self.__user_repository = user_use_case
        self.__class_user_case = class_user_case

    def register(
        self, user_name: str, user_nickname: str, user_class_id: int, user_role: int
    ) -> None:
        # Validar se o nickname já existe
        self.__user_nickname_exists(user_nickname=user_name)

        # Validar a string
        self.__validate_name(user_name)
        # self.__validate_name(user_nickname)

        # Certifica se existe a classe buscando do repositório da Classe.
        self.__user_class_exists(user_class_id)

        self.__user_repository.insert_user(
            user_name=user_name,
            user_nickname=user_nickname,
            user_class_id=user_class_id,
            user_role=user_role,
        )

    def __user_nickname_exists(self, user_nickname: str) -> None:
        if self.__user_repository.nick_name_exists(user_nickname):
            raise Exception("O username já existe.")

    @classmethod
    def __validate_name(cls, name: str) -> None:
        if not name.isalpha():
            raise Exception("Deve conter só letra.")

    def __user_class_exists(self, class_id: int) -> None:
        if not self.__class_user_case.exists(class_id=class_id):
            raise Exception("Essa classe não existe.")
