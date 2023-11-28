from sqlalchemy import Boolean, Column, Integer, String
from game.infra.db.settings.base import Base


class ClassEntity(Base):
    __tablename__ = "classes"

    class_id = Column(Integer, autoincrement=True, primary_key=True)
    class_name = Column(String, nullable=False)
    class_active = Column(Boolean, default=True)

    def __repr__(self):
        return f"Class [class_id={self.class_id}, class_name={self.class_name}, class_active={self.class_active}]"

    @classmethod
    def create_table(cls, engine):
        Base.metadata.create_all(engine)
