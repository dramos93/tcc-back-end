from game.infra.db.repositories.authentication_repository.authentication_repository import AuthenticationRepository


def test_create_authentication():
    authentication_repository = AuthenticationRepository()
    authentication_repository.create(user_id=1)


def test_get_token():
    authentication_repository = AuthenticationRepository()
    authentication_repository.get_token(user_id=1)
    

def test_logout():
    authentication_repository = AuthenticationRepository()
    token = authentication_repository.get_token(user_id=1).token
    authentication_repository.logout(user_id=1, token=token)
    user_id_without_token = authentication_repository.get_token(user_id=1)
    assert user_id_without_token is None

