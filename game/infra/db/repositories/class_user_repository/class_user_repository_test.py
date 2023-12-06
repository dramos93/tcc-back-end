import pytest
from .class_user_repository import ClassUserRepository

class_user_repository = ClassUserRepository()


@pytest.mark.skip("Pra não ficar criando dados.")
def test_create_class_user():
    assert class_user_repository.create(1, 1)


def test_get_classes():
    assert class_user_repository.get_classes(user_id=1)
