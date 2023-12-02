from game.infra.db.repositories.authentication_repository.authentication_repository import (
    AuthenticationRepository,
)

authentication_repository = AuthenticationRepository()
token = authentication_repository.create(user_id=1).token


def test_create_authentication():
    user_id = 1
    token = authentication_repository.create(user_id=user_id).token
    authentication_repository.logout(user_id=user_id, token=token)
    user_with_token = authentication_repository.get_credentials_from_token(token=token)
    assert user_with_token.active == False
    assert user_with_token.token == token


def test_get_token():
    authentication_repository.get_credentials_from_token(token=token)
