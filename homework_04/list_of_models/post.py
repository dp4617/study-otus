from sqlalchemy import (
    Column,
    String,
    Text,
    Integer,
    ForeignKey,
)
from sqlalchemy.orm import relationship

from .base import Base
from .mixins import CreatedAtMixin


class Post(CreatedAtMixin,Base):

    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("User.id"), nullable=False)
    title = Column(String(256), nullable=False, default='', server_default='')
    body = Column(Text, nullable=False, default="", server_default="")

    user = relationship("User", back_populates='posts')