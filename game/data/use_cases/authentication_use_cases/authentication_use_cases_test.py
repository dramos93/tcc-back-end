from uuid import uuid1
import pytest
from game.data.use_cases.authentication_use_cases.authentication_use_cases import (
    AuthenticationUseCases,
)
from game.infra.db.repositories.authentication_repository.authentication_repository_mock import (
    AuthenticationRepositoryMock,
)
from game.infra.db.repositories.users_repository.users_repository_mock import (
    UsersRepositoryMock,
)


authentication_repository_mock = AuthenticationRepositoryMock()
user_repository_mock = UsersRepositoryMock()
authentication_use_case = AuthenticationUseCases(
    authentication_repository_mock, user_repository_mock
)


def test_create_authentication_user_case():
    authentication_use_case.create_token(user_id=1, user_password="123456")


def test_get_token():
    user_id = 1
    token_repository = authentication_repository_mock.get_token(user_id=user_id).token
    token = authentication_use_case.get_token(user_id=user_id)
    assert token_repository == token["token"]


def test_logout():
    user_id = 1
    token = authentication_repository_mock.get_token(user_id=user_id).token
    authentication_use_case.logout(user_id=user_id, token=token)


def test_user_not_found():
    with pytest.raises(Exception, match="Usuário não encontrado."):
        authentication_use_case.get_token(user_id=999)

    with pytest.raises(Exception, match="Usuário não encontrado."):
        authentication_use_case.logout(user_id=999, token=uuid1())


def test_user_no_login():
    with pytest.raises(Exception, match="Usuário ou senha não existe."):
        authentication_use_case.create_token(user_id=1, user_password="ABC")
