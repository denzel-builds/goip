from pydantic import BaseModel, HttpUrl
from typing import Optional
from datetime import date, datetime

#Base properties shared across multiple schemas
class OpportunityBase(BaseModel):
    title: str
    company: str
    type: str
    description: Optional[str] = None
    requirements: Optional[str] = None
    deadline: Optional[date] = None
    location: Optional[str] = None
    url: Optional[HttpUrl] = None # Pydantic will validate that the URL is in a proper format

# Used for POST. It inherits everything from OpportunityBase.
class OpportunityCreate(OpportunityBase):
        pass

# Used for PUT. All fields are optional so you can update only the fields you want.
class OpportunityUpdate(BaseModel):
        title: Optional[str] = None
        company: Optional[str] = None
        type: Optional[str] = None
        description: Optional[str] = None
        requirements: Optional[str] = None
        deadline: Optional[date] = None
        location: Optional[str] = None
        url: Optional[HttpUrl] = None

# Used for Response. It adds the DB-generated fields like id and created_at to the base schema.
class OpportunityResponse(OpportunityBase):
    id: int
    created_at: datetime

    class Config:
        # This tells Pydantic to read the data even if it is not a dict, but an ORM model (like SQLAlchemy).
        # (This is necessary for FastAPI to work seamlessly with SQLAlchemy models.
        from_attributes = True
