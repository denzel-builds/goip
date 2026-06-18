from sqlalchemy import Column, Integer, String, DateTime, Text, Date
from sqlalchemy.sql import func
from app.database import Base

class Opportunity(Base):
    __tablename__ = "opportunities"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    company = Column(String(255), nullable=False)
    type = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    requirements = Column(Text, nullable=True)
    deadline = Column(Date, nullable=True)
    location = Column(String(255), nullable=True)
    url = Column(String(255), nullable=True)

    #Automatically records the timestamp when a new record is created
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    