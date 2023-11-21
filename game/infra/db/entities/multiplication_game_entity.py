from sqlalchemy import Column, Integer
from game.infra.db.settings.base import Base


class MultiplicationGameEntity(Base):
    __tablename__ = "multiplication_game"

    user_id = Column(Integer, primary_key=True, nullable=False)
    class_id = Column(Integer, primary_key=True, nullable=False)
    multiplication_table = Column(Integer, primary_key=True, nullable=False)
    round = Column(Integer, primary_key=True, nullable=False)
    errors = Column(Integer, nullable=True)

    def __repr__(self):
        return f"Multiplication Game [user_id={self.user_id}, class_id={self.class_id}, multiplication_table={self.multiplication_table}, round={self.round}, errors={self.errors}]"

    @classmethod
    def create_table(cls, engine):
        Base.metadata.create_all(engine)
    