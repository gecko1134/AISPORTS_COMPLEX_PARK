from sqlalchemy import Column, String, Integer, DateTime, func
from .base import Base

class UsageMetrics(Base):
    __tablename__ = "usage_metrics"
    id = Column(String, primary_key=True)
    tenant_id = Column(String)
    timestamp = Column(DateTime, default=func.now())
    total_bookings = Column(Integer)
    total_facilities = Column(Integer)
