from sqlalchemy import insert, select
from game.infra.db.entities.class_entity import ClassEntity
from game.infra.db.entities.user_entity import UsersEntity
from game.infra.db.settings.connection import DBConnectionHandler
from game.domain.models.class_user_model import ClassUserModel
from game.infra.db.entities.class_user_entity import ClassUserEntity


class ClassUserRepository:
    @classmethod
    def create(cls, class_id: int, user_id: int) -> ClassUserModel:
        with DBConnectionHandler() as db:
            engine = db.get_engine()
            ClassUserEntity.create_table(engine=engine)
            ClassEntity.create_table(engine=engine)
            UsersEntity.create_table(engine=engine)
            breakpoint()
            class_user = (
                insert(ClassUserEntity)
                .values(class_id=class_id, user_id=user_id)
                .returning(ClassUserEntity)
            )
            try:
                data = db.session.execute(class_user).scalar()
                db.session.commit()

            except Exception as exception:
                db.session.rollback()
                raise exception

        return data

    @classmethod
    def get_classes(cls, user_id: int) -> ClassUserModel:
        with DBConnectionHandler() as db:
            engine = db.get_engine()
            ClassUserEntity.create_table(engine=engine)

            class_user = select(ClassUserEntity).filter(
                ClassUserEntity.user_id == user_id
            )
            try:
                data = db.session.execute(class_user).scalar()
                db.session.commit()

            except Exception as exception:
                db.session.rollback()
                raise exception

        return data
