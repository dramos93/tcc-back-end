from game.infra.db.repositories.users_repository.users_repository_mock import UsersRepositoryMock
from datetime import datetime
import pytest
from .user_register import UserRegisterUseCase

def test_user_register_use_case():
    users_repository = UsersRepositoryMock()
    user_register_use_case = UserRegisterUseCase(use_case=users_repository)

    user_register_use_case.register(
        user_name="Daniel",
        user_nickname=f"dramo93_{datetime.now().strftime('%M%S')}",
        user_class_id=123,
        user_role=1
        )

def test_user_nickname_exists():
    users_repository = UsersRepositoryMock()
    user_register_use_case = UserRegisterUseCase(use_case=users_repository)

    try:
        user_register_use_case.register(
            user_name="Daniel",
            user_nickname=f"dramo93",
            user_class_id=123,
            user_role=1
            )
    except:
        assert pytest.raises(Exception, match="O username já existe.")
        
def test_user_name_contains_number():
    users_repository = UsersRepositoryMock()
    user_register_use_case = UserRegisterUseCase(use_case=users_repository)

    try: 
        user_register_use_case.register(
            user_name="Daniel1",
            user_nickname="new_dramos93",
            user_class_id=123,
            user_role=1
            )
    except:
        assert pytest.raises(Exception, match="Deve conter só letra.")


def test__user_class_exists():
    pass
    # users_repository = UsersRepository()
    # user_register_use_case = UserRegisterUseCase(use_case=users_repository)

    # try: 
    #     user_register_use_case.register(user_name="Daniel1", user_nickname="new_dramos93", user_class_id=123, user_role=1)
    # except:
    #     assert pytest.raises(Exception, match="Deve conter só letra.")

    