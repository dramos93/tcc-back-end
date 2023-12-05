from sqlalchemy import Column, ForeignKey, Integer
from game.infra.db.settings.base import Base


class ClassUserEntity(Base):
    __tablename__ = "class_user"

    class_id = Column(Integer, ForeignKey("classes.class_id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)

    @classmethod
    def create_table(cls, engine):
        Base.metadata.create_all(engine)
