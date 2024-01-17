from game.infra.db.repositories.class_repository.class_repository import ClassRepository
from game.infra.db.repositories.users_repository.users_repository import UsersRepository
from game.data.use_cases.user_use_cases.user_use_case import UserUseCase
from game.presentation.controllers.user_controller.user_controller import (
    CreateUserController,
)


def create_user_composer():
    user_repository = UsersRepository()
    class_repository = ClassRepository()
    use_case = UserUseCase(user_repository, class_repository)
    controller = CreateUserController(use_case)
    return controller.create


def handle_user_composer():
    user_repository = UsersRepository()
    use_case = UserUseCase(user_repository)
    controller = CreateUserController(use_case)
    return controller.handle
