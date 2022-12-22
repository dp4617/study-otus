from sqlalchemy import (
    Column,
    String,
    Integer,
)
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import CreatedAtMixin


# class User(Base):
class User(CreatedAtMixin,Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(String(32), default='')
    username = Column(String(32), unique=True)
    email = Column(String(32), unique=True)

    posts = relationship("Post", back_populates='user')

    def __str__(self):
        return f"User(id={self.id}, username={self.username!r})"