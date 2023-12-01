from game.infra.db.repositories.authentication_repository.authentication_repository import (
    AuthenticationRepository,
)
from game.data.use_cases.authentication_use_cases.authentication_use_cases import (
    AuthenticationUseCases,
)
from game.infra.db.repositories.users_repository.users_repository import UsersRepository
from game.presentation.controllers.authentication_controller.authentication_controller import (
    AuthenticationController,
)


def create_token_composer():
    authentication_repository = AuthenticationRepository()
    user_repository = UsersRepository()
    use_cases = AuthenticationUseCases(authentication_repository, user_repository)
    controller = AuthenticationController(use_cases)
    return controller.create_token


def get_token_composer():
    authentication_repository = AuthenticationRepository()
    user_repository = UsersRepository()
    use_cases = AuthenticationUseCases(authentication_repository, user_repository)
    controller = AuthenticationController(use_cases)
    return controller.get_token


def logout_composer():
    authentication_repository = AuthenticationRepository()
    user_repository = UsersRepository()
    use_cases = AuthenticationUseCases(authentication_repository, user_repository)
    controller = AuthenticationController(use_cases)
    return controller.logout
