from sqlalchemy import Column, String, DateTime, func
from .base import Base

class AuditLog(Base):
    __tablename__ = "audit_logs"
    id = Column(String, primary_key=True)
    actor = Column(String)
    action = Column(String)
    entity = Column(String)
    timestamp = Column(DateTime, default=func.now())
    detail = Column(String)
