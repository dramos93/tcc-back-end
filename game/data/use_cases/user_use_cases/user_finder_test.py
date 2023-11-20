import pytest
from game.infra.db.repositories.users_repository.users_repository import UsersRepository
from .user_finder import UserFinder

def test_user_finder():
    users_repository = UsersRepository()
    user_finder = UserFinder(users_repository)
    user = user_finder.find(1)
    assert user
    assert type(user["user_id"]) == int

def test_use_not_found():
    users_repository = UsersRepository()
    user_finder = UserFinder(users_repository)
    try:
        user_finder.find(3)
    except:
        assert pytest.raises(Exception, match="Usuário não encontrado.")

    