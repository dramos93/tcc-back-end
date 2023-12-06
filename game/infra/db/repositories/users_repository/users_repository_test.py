from game.infra.db.repositories.users_repository.users_repository import UsersRepository
import pytest


@pytest.mark.skip(reason="Porque eu quis.")
def test_create_user():
    user_repository = UsersRepository()
    user_repository.insert_user(
        user_name="Daniel",
        user_nickname="dramos933",
        user_password="123456",
        user_role=1,
    )


def test_get_all():
    user_repository = UsersRepository()
    print()
    print(user_repository.get_all_users())


def test_get_by_id():
    user_repository = UsersRepository()
    print()
    user_repository_result = user_repository.get_user_by_id(1)
    assert user_repository_result.user_id == 1
    assert user_repository_result.user_name == "Daniel"
    assert user_repository_result.user_nickname == "dramos933"
    assert user_repository_result.user_role == 1
    assert user_repository_result.user_active == 1


def test_get_by_id_not_found():
    user_repository = UsersRepository()
    assert user_repository.get_user_by_id(10000) is None


def test_nick_name_exists():
    users_repository = UsersRepository()
    print()
    assert users_repository.nick_name_exists("dramos933")
    assert users_repository.nick_name_exists("qualquer") == False


def test_login():
    users_repository = UsersRepository()
    assert users_repository.login(user_id=1, user_password="123456")
