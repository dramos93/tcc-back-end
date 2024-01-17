from game.data.use_cases.classes_use_case.classes_use_case import ClassesUseCase
from game.infra.db.repositories.class_repository.class_repository import ClassRepository
from game.infra.db.repositories.class_user_repository.class_user_repository import (
    ClassUserRepository,
)
from game.infra.db.repositories.multiplication_game_repository.multiplication_game_repository import (
    MultiplicationGameRepository,
)
from game.infra.db.repositories.users_repository.users_repository import UsersRepository
from game.presentation.controllers.class_controller.class_controller import (
    ClassesController,
)


def get_class_composer():
    class_repository = ClassRepository()
    user_repository = UsersRepository()
    game_repository = MultiplicationGameRepository()
    class_user_repository = ClassUserRepository()

    classes_use_case = ClassesUseCase(
        class_repository=class_repository,
        user_repository=user_repository,
        game_repository=game_repository,
        class_user_repository=class_user_repository,
    )
    classes_controller = ClassesController(use_case=classes_use_case)
    return classes_controller.get_class
