from sqlalchemy import Boolean, Column, Integer, String
from game.infra.db.settings.base import Base


class UsersEntity(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, autoincrement=True)
    user_class_id = Column(Integer)
    user_name = Column(String, nullable=False)
    user_nickname = Column(String, unique=True)
    user_password = Column(String)
    user_role = Column(Integer, nullable=False, default=1)
    user_active = Column(Boolean, nullable=False, default=True)

    def __repr__(self):
        return f"User [id={self.user_id}, nickname={self.user_nickname}, class_id={self.user_class_id}]"

    @classmethod
    def create_table(cls, engine):
        Base.metadata.create_all(engine)
