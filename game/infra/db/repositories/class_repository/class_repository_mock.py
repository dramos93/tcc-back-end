from game.data.interfaces.class_repository_interface import ClassRepositoryInterface
from game.domain.models.class_model import ClassModel


class ClassRepositoryMock(ClassRepositoryInterface):
    @classmethod
    def create(cls, class_name: str) -> None:
        pass

    @classmethod
    def get_by_id(cls, class_id: int) -> ClassModel:
        class_fake = {
            1: ClassModel(class_id=1, class_name="1ª Série", class_active=True),
            2: ClassModel(class_id=2, class_name="2ª Série", class_active=True),
        }
        return class_fake[class_id]

    @classmethod
    def exists(cls, class_id: int) -> bool:
        class_ids = [1, 2]
        return True if class_id in class_ids else False
