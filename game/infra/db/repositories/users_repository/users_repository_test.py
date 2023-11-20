from game.infra.db.repositories.users_repository.users_repository import UsersRepository
import pytest 

@pytest.mark.skip(reason="Porque eu quis.")
def test_create_user():
    user_repository = UsersRepository()
    user_repository.insert_user(
        user_class_id=1,
        user_name="Daniel",
        user_nickname="dramos933",
        user_password="123456",
        user_role=1)
    
def test_get_all():
    user_repository = UsersRepository()
    print()
    print(user_repository.get_all_users())
    
def test_get_by_id():
    user_repository = UsersRepository()
    print()
    user_repository= user_repository.get_user_by_id(1)
    assert user_repository.user_id == 1
    assert user_repository.user_class_id == 1
    assert user_repository.user_name == "Daniel"
    assert user_repository.user_nickname == "dramos933"
    assert user_repository.user_role == 1
    assert user_repository.user_active == 1

    print()

def test_nick_name_exists():
    users_repository = UsersRepository()
    print()
    assert users_repository.nick_name_exists("dramos933")
    assert users_repository.nick_name_exists("qualquer") == False
