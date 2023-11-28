import pytest
from .class_repository import ClassRepository


@pytest.mark.skip("Para não salvar mais no banco.")
def test_create_class_repository():
    class_repository = ClassRepository()
    class_repository.create(class_name="1º Série - Matutino")


def test_get_by_id():
    class_id = 1
    class_repository = ClassRepository()
    class_entity = class_repository.get_by_id(class_id=class_id)
    print()
    print(class_entity.class_id)
    print(class_entity.class_name)
    print(class_entity.class_active)


def test_exist():
    class_id = 9999
    class_repository = ClassRepository()
    class_entity = class_repository.exists(class_id=class_id)

    print()
    print(class_entity)
    print(type(class_entity))
