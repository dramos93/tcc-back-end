from game.infra.db.repositories.authentication_repository.authentication_repository import AuthenticationRepository
from game.infra.db.repositories.class_repository.class_repository import ClassRepository
from game.infra.db.repositories.multiplication_game_repository.multiplication_game_repository import (
    MultiplicationGameRepository,
)
from game.data.use_cases.multiplication_game_use_cases.multiplication_game_use_cases import (
    MultiplicationGameUseCase,
)
from game.infra.db.repositories.users_repository.users_repository import UsersRepository
from game.presentation.controllers.multiplication_game.multiplication_game_controller import (
    MultiplicationGameController,
)


def create_multiplication_game_composer():
    multiplication_game_repository = MultiplicationGameRepository()
    user_repository = UsersRepository()
    class_repository = ClassRepository()
    authentication_repository = AuthenticationRepository()
    authentication_use_cases = authentication_use_cases(authentication_repository, user_repository)

    multiplication_game_use_cases = MultiplicationGameUseCase(
        multiplication_game_repository, user_repository, class_repository
    )
    multiplication_game_controller = MultiplicationGameController(
        multiplication_game_use_cases, authentication_use_cases
    )
    return multiplication_game_controller.create_multiplication_game


def get_all_multiplication_game_composer():
    multiplication_game_repository = MultiplicationGameRepository()
    user_repository = UsersRepository()
    class_repository = ClassRepository()
    authentication_repository = AuthenticationRepository()
    authentication_use_cases = authentication_use_cases(authentication_repository, user_repository)

    multiplication_game_use_cases = MultiplicationGameUseCase(
        multiplication_game_repository, user_repository, class_repository
    )
    multiplication_game_controller = MultiplicationGameController(
        multiplication_game_use_cases, authentication_use_cases
    )
    return multiplication_game_controller.get_all_multiplication_game
