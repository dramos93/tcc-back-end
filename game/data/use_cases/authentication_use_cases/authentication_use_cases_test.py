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
    token_repository = authentication_repository_mock.create(user_id=user_id).token
    token = authentication_use_case.get_user_permissions(token=token_repository)
    assert token_repository == token["token"]


def test_logout():
    user_id = 1
    token = authentication_repository_mock.create(user_id=user_id).token
    authentication_use_case.logout(user_id=user_id, token=token)


def test_user_not_found():
    with pytest.raises(Exception, match="Usuário não encontrado."):
        authentication_use_case.logout(user_id=999, token=uuid1())


def test_user_no_login():
    with pytest.raises(Exception, match="Usuário ou senha não existe."):
        authentication_use_case.create_token(user_id=1, user_password="ABC")


def test_get_role_from_user_with_toke():
    auth_repo = authentication_repository_mock.create(1)
    user = user_repository_mock.get_user_by_id(1)
    token = auth_repo.token
    permissions = authentication_use_case.get_user_permissions(token=token)
    assert permissions["user_id"] == auth_repo.user_id
    assert permissions["token"] == auth_repo.token
    assert permissions["created_on"] == auth_repo.created_on
    assert permissions["active"] == auth_repo.active
    if user:
        assert permissions["class_id"] == user.user_class_id
        assert permissions["user_name"] == user.user_name
        assert permissions["user_nickname"] == user.user_nickname
        assert permissions["user_role"] == user.user_role
    else:
        assert False
