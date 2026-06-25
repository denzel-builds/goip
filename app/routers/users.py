from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.application import SavedOpportunity
from app.models.opportunity import Opportunity
from app.models.user import User
from app.schemas.application import SavedOpportunityResponse
from app.services.auth_service import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/saved/{opportunity_id}", response_model=SavedOpportunityResponse, status_code=status.HTTP_201_CREATED)
def save_opportunity(
    opportunity_id: int, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    opp = db.query(Opportunity).filter(Opportunity.id == opportunity_id).first()
    if not opp:
        raise HTTPException(status_code=404, detail="Opportunity not found")
        
    existing = db.query(SavedOpportunity).filter(
        SavedOpportunity.user_id == current_user.id, 
        SavedOpportunity.opportunity_id == opportunity_id
    ).first()
    
    if existing:
        raise HTTPException(status_code=400, detail="Opportunity already saved")
        
    saved_opp = SavedOpportunity(user_id=current_user.id, opportunity_id=opportunity_id)
    db.add(saved_opp)
    db.commit()
    db.refresh(saved_opp)
    return saved_opp

@router.get("/saved", response_model=List[SavedOpportunityResponse])
def list_saved_opportunities(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(SavedOpportunity).filter(SavedOpportunity.user_id == current_user.id).all()

@router.delete("/saved/{opportunity_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_saved_opportunity(
    opportunity_id: int, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    saved_opp = db.query(SavedOpportunity).filter(
        SavedOpportunity.user_id == current_user.id, 
        SavedOpportunity.opportunity_id == opportunity_id
    ).first()
    
    if not saved_opp:
        raise HTTPException(status_code=404, detail="Saved opportunity not found")
        
    db.delete(saved_opp)
    db.commit()
    return