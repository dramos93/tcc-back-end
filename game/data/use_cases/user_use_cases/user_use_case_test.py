from game.infra.db.repositories.class_repository.class_repository_mock import (
    ClassRepositoryMock,
)
from game.infra.db.repositories.users_repository.users_repository_mock import (
    UsersRepositoryMock,
)
import pytest
from .user_use_case import UserUseCase
from datetime import datetime

users_repository = UsersRepositoryMock()
class_repository = ClassRepositoryMock()


def test_user_register_use_case():
    user_register_use_case = UserUseCase(
        user_use_case=users_repository, class_user_case=class_repository
    )

    user_register_use_case.register(
        user_name="Daniel",
        user_nickname=f"dramo93_{datetime.now().strftime('%M%S')}",
        user_class_id=1,
        user_role=1,
        user_password="123456",
    )


def test_user_nickname_exists():
    with pytest.raises(Exception, match="O username já existe."):
        user_register_use_case = UserUseCase(
            user_use_case=users_repository, class_user_case=class_repository
        )
        user_register_use_case.register(
            user_name="Daniel",
            user_nickname="dramos93",
            user_class_id=1,
            user_role=1,
            user_password="123456",
        )


def test_user_name_contains_number():
    with pytest.raises(Exception, match="Deve conter só letra."):
        user_register_use_case = UserUseCase(
            user_use_case=users_repository, class_user_case=class_repository
        )
        user_register_use_case.register(
            user_name="Daniel1",
            user_nickname="new_dramos93",
            user_class_id=123,
            user_role=1,
            user_password="123456",
        )


def test_user_class_exists():
    with pytest.raises(Exception, match="Essa classe não existe."):
        user_register_use_case = UserUseCase(
            user_use_case=users_repository, class_user_case=class_repository
        )
        user_register_use_case.register(
            user_name="Daniel",
            user_nickname="new_dramos93",
            user_class_id=1230,
            user_role=1,
            user_password="123456",
        )


def test_user_finder():
    user_finder = UserUseCase(users_repository, class_repository)
    user = user_finder.find(1)
    assert user
    assert type(user["user_id"]) == int


def test_use_not_found():
    with pytest.raises(Exception, match="Usuário não encontrado."):
        user_finder = UserUseCase(users_repository, class_repository)
        user_finder.find(3)
