from typing import List
from sqlalchemy import insert, select
from sqlalchemy.exc import SQLAlchemyError
from game.data.interfaces.class_user_repository_interface import (
    ClassUserRepositoryInterface,
)
from game.infra.db.entities.class_entity import ClassEntity
from game.infra.db.entities.user_entity import UsersEntity
from game.infra.db.settings.connection import DBConnectionHandler
from game.domain.models.class_user_model import ClassUserModel
from game.infra.db.entities.class_user_entity import ClassUserEntity


class ClassUserRepository(ClassUserRepositoryInterface):
    @classmethod
    def create(cls, class_id: int, user_id: int) -> ClassUserModel:
        with DBConnectionHandler() as db:
            engine = db.get_engine()
            ClassUserEntity.create_table(engine=engine)
            ClassEntity.create_table(engine=engine)
            UsersEntity.create_table(engine=engine)
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
    def get_classes(cls, user_id: int) -> List[ClassUserModel]:
        with DBConnectionHandler() as db:
            engine = db.get_engine()
            UsersEntity.create_table(engine=engine)
            ClassUserEntity.create_table(engine=engine)

            class_user = select(ClassUserEntity).filter(
                ClassUserEntity.user_id == user_id
            )
            try:
                data = db.session.execute(class_user).scalars().all()

            except SQLAlchemyError as exception:
                db.session.rollback()
                raise exception

        return list(data)

    @classmethod
    def get_users_from_class(cls, class_id: int) -> List[ClassUserModel]:
        with DBConnectionHandler() as db:
            engine = db.get_engine()
            ClassUserEntity.create_table(engine=engine)

            class_user = select(ClassUserEntity).filter(
                ClassUserEntity.class_id == class_id
            )
            try:
                data = db.session.execute(class_user).scalars().all()

            except Exception as exception:
                db.session.rollback()
                raise exception

        return list(data)
