
import uuid
from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime, func
from configurations.db.main import Base


class BaseModel(Base):
    __abstract__ = True
    id = Column(String(36), primary_key=True,
                default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())
    deleted_at = Column(DateTime, nullable=True)
    is_deleted = Column(Boolean, default=False)
