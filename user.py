from sqlalchemy import Column, String, ForeignKey, DateTime, func
from .base import Base

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    tenant_id = Column(String, ForeignKey("tenants.id"), nullable=False)
    role = Column(String)
    created_at = Column(DateTime, default=func.now())
