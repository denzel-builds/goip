import enum
from sqlalchemy import Column, Integer, ForeignKey, Enum, Text, DateTime
from sqlalchemy.sql import func
from app.database import Base

# Enforce strict status values
class ApplicationStatus(str, enum.Enum):
    APPLIED = "Applied"
    ASSESSMENT = "Assessment"
    INTERVIEW = "Interview"
    OFFER = "Offer"
    REJECTED = "Rejected"

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    # ondelete="CASCADE" ensures if a user or opportunity is deleted, the application is too
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    opportunity_id = Column(Integer, ForeignKey("opportunities.id", ondelete="CASCADE"), nullable=False)
    
    status = Column(Enum(ApplicationStatus), default=ApplicationStatus.APPLIED)
    notes = Column(Text, nullable=True)
    applied_at = Column(DateTime(timezone=True), server_default=func.now())

class SavedOpportunity(Base):
    __tablename__ = "saved_opportunities"

    # A user can only save a specific opportunity once, so the combination of both is the primary key
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    opportunity_id = Column(Integer, ForeignKey("opportunities.id", ondelete="CASCADE"), primary_key=True)
    saved_at = Column(DateTime(timezone=True), server_default=func.now())