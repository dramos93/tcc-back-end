from datetime import date
import uuid
from sqlalchemy import UUID, Boolean, Column, Date, ForeignKey, Integer
from game.infra.db.settings.base import Base


class AuthenticationEntity(Base):
    __tablename__ = "authentication"

    token = Column(UUID, primary_key=True, nullable=False, default=uuid.uuid1())
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    created_on = Column(Date, default=date.today(), nullable=False)
    active = Column(Boolean, default=True, nullable=False)

    @classmethod
    def create_table(cls, engine):
        Base.metadata.create_all(engine)
