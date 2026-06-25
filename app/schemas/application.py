from pydantic import BaseModel
from typing import Optional
from datetime import datetime
from app.models.application import ApplicationStatus

# --- Application Schemas ---
class ApplicationCreate(BaseModel):
    opportunity_id: int
    notes: Optional[str] = None

class ApplicationUpdate(BaseModel):
    status: ApplicationStatus
    notes: Optional[str] = None

class ApplicationResponse(BaseModel):
    id: int
    user_id: int
    opportunity_id: int
    status: ApplicationStatus
    notes: Optional[str]
    applied_at: datetime

    class Config:
        from_attributes = True

# --- Saved Opportunity Schemas ---
class SavedOpportunityResponse(BaseModel):
    user_id: int
    opportunity_id: int
    saved_at: datetime

    class Config:
        from_attributes = True