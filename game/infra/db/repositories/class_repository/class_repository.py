from sqlalchemy import select
from game.data.interfaces.class_repository_interface import ClassRepositoryInterface
from game.domain.models.class_model import ClassModel
from game.infra.db.entities.class_entity import ClassEntity
from game.infra.db.settings.connection import DBConnectionHandler


class ClassRepository(ClassRepositoryInterface):

    @classmethod
    def create(cls, class_name: str, class_active: bool = True):
        with DBConnectionHandler() as db:
            try:
                engine = db.get_engine()
                ClassEntity.create_table(engine=engine)

                new_class = ClassEntity(class_name=class_name, class_active=class_active)
                
                db.session.add(new_class)
                db.session.commit()
            except Exception as exception:
                db.session.rollback()
                raise exception

    @classmethod
    def get_by_id(cls, class_id: int) -> ClassModel:
        with DBConnectionHandler() as db:
            try:
                query = select(ClassEntity).filter(ClassEntity.class_id == class_id)
                class_entity = db.session.execute(query).scalar()

                return class_entity
            except Exception as exception:
                db.session.rollback()
                raise exception
            
    @classmethod
    def exists(cls, class_id) -> bool:
        with DBConnectionHandler() as db:
            try:
                query = select(ClassEntity).where(ClassEntity.class_id == class_id).exists()

                return db.session.query(query).scalar()
            except Exception as exception:
                db.session.rollback()
                raise exception
        