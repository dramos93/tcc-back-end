from game.infra.db.repositories.users_repository import UsersRepository
import pytest 

@pytest.mark.skip("Porque eu quis.")
def test_create_user():
    user_repository = UsersRepository()
    user_repository.insert_user(
        user_class_id=1,
        user_name="Daniel",
        user_nickname="dramos93",
        user_role=1
        )

def test_get_all():
    user_repository = UsersRepository()
    print()
    print(user_repository.get_all_users())

def test_get_by_id():
    user_repository = UsersRepository()
    print()
    print(user_repository.get_user_by_id(1))
