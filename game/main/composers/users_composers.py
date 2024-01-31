from game.data.use_cases.authentication_use_cases.authentication_use_cases import (
    AuthenticationUseCases,
)
from game.infra.db.repositories.authentication_repository.authentication_repository import (
    AuthenticationRepository,
)
from game.infra.db.repositories.users_repository.users_repository import UsersRepository
from game.data.use_cases.user_use_cases.user_use_case import UserUseCase
from game.presentation.controllers.user_controller.user_controller import (
    CreateUserController,
)


def create_user_composer():
    user_repository = UsersRepository()
    authentication_repository = AuthenticationRepository()
    use_case = UserUseCase(user_repository)
    auth_case = AuthenticationUseCases(authentication_repository, user_repository)
    controller = CreateUserController(use_case, auth_case)
    return controller.create


def handle_user_composer():
    user_repository = UsersRepository()
    authentication_repository = AuthenticationRepository()
    authentication_use_cases = authentication_use_cases(
        authentication_repository, user_repository
    )
    use_case = UserUseCase(user_repository)
    controller = CreateUserController(use_case)
    return controller.handle
