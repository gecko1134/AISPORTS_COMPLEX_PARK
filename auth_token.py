from sqlalchemy import Column, String, DateTime
from .base import Base

class AuthToken(Base):
    __tablename__ = "auth_tokens"
    id = Column(String, primary_key=True)
    tenant_id = Column(String)
    user_id = Column(String)
    token = Column(String)
    expires_at = Column(DateTime)
