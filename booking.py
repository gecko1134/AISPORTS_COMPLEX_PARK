from sqlalchemy import Column, String, DateTime, ForeignKey, Integer, func
from sqlalchemy.orm import relationship
from .base import Base

class Facility(Base):
    __tablename__ = "facilities"
    id = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String)
    capacity = Column(Integer)
    created_at = Column(DateTime, default=func.now())

class Booking(Base):
    __tablename__ = "bookings"
    id = Column(String, primary_key=True)
    facility_id = Column(String, ForeignKey("facilities.id"), nullable=False)
    user_id = Column(String, nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    status = Column(String, default="confirmed")
    created_at = Column(DateTime, default=func.now())
    facility = relationship("Facility")
