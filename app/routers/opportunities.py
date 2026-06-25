from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_
from typing import List, Optional
from datetime import date

from app.database import get_db
from app.models.opportunity import Opportunity
from app.schemas.opportunity import OpportunityCreate, OpportunityUpdate, OpportunityResponse
from app.services.auth_service import get_current_user
from app.models.user import User

# Initialize the router
router = APIRouter(
    prefix="/opportunities",
    tags=["Opportunities"]
)

@router.post("/", response_model=OpportunityResponse, status_code=201)
def create_opportunity(
    opportunity: OpportunityCreate, 
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user) 
):
    # Convert Pydantic schema to SQLAlchemy model
    db_opp = Opportunity(**opportunity.model_dump())
    db.add(db_opp)
    db.commit()
    db.refresh(db_opp)
    return db_opp

@router.get("/", response_model=List[OpportunityResponse])
def get_opportunities(
    type: Optional[str] = None,
    company: Optional[str] = None,
    search: Optional[str] = None,
    deadline_before: Optional[date] = None,
    db: Session = Depends(get_db)
):
    # Start with a base query
    query = db.query(Opportunity)

    # Dynamically apply filters if the user provided them
    if type:
        query = query.filter(Opportunity.type == type)
    if company:
        query = query.filter(Opportunity.company == company)
    if deadline_before:
        query = query.filter(Opportunity.deadline < deadline_before)
    if search:
        # Search across title, description, and requirements using 'ilike' (case-insensitive)
        query = query.filter(
            or_(
                Opportunity.title.ilike(f"%{search}%"),
                Opportunity.description.ilike(f"%{search}%"),
                Opportunity.requirements.ilike(f"%{search}%")
            )
        )

    # Execute the query and return results
    return query.all()

@router.get("/{id}", response_model=OpportunityResponse)
def get_opportunity(id: int, db: Session = Depends(get_db)):
    db_opp = db.query(Opportunity).filter(Opportunity.id == id).first()
    if not db_opp:
        raise HTTPException(status_code=404, detail="Opportunity not found")
    return db_opp

@router.put("/{id}", response_model=OpportunityResponse)
def update_opportunity(id: int, opportunity: OpportunityUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_opp = db.query(Opportunity).filter(Opportunity.id == id).first()
    if not db_opp:
        raise HTTPException(status_code=404, detail="Opportunity not found")

    # Only update the fields the user actually sent
    update_data = opportunity.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_opp, key, value)

    db.commit()
    db.refresh(db_opp)
    return db_opp

@router.delete("/{id}", status_code=204)
def delete_opportunity(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_opp = db.query(Opportunity).filter(Opportunity.id == id).first()
    if not db_opp:
        raise HTTPException(status_code=404, detail="Opportunity not found")

    db.delete(db_opp)
    db.commit()
    return # 204 No Content response