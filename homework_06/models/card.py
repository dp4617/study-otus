from .database import db
from sqlalchemy import Column, Text, String, Boolean, DateTime, func


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True, default="", server_default="")
    created_at = Column(DateTime, server_default=func.now())
    body = Column(Text, nullable=False, default="", server_default="")
