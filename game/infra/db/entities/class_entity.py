from sqlalchemy import Boolean, Column, Integer, String
from game.infra.db.settings.base import Base

class ClassEntity(Base):
    __tablename__ = 'classes'

    class_id = Column(Integer, autoincrement=True, primary_key=True)
    class_name = Column(String, nullable=False)
    class_active = Column(Boolean, default=True)


    @classmethod
    def create_table(cls, engine):
        Base.metadata.create_all(engine)
    