import uuid

from sqlalchemy import Column, DateTime, String
from sqlalchemy.sql import func

from src.core.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    name = Column(
        String(255),
        nullable=False
    )

    email = Column(
        String(255),
        unique=True,
        nullable=False
    )

    registration_date = Column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )