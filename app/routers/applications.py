from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.application import Application
from app.models.opportunity import Opportunity
from app.models.user import User
from app.schemas.application import ApplicationCreate, ApplicationUpdate, ApplicationResponse
from app.services.auth_service import get_current_user

router = APIRouter(prefix="/applications", tags=["Applications"])

@router.post("/", response_model=ApplicationResponse, status_code=status.HTTP_201_CREATED)
def track_application(
    app_in: ApplicationCreate, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    # Verify the opportunity actually exists
    opp = db.query(Opportunity).filter(Opportunity.id == app_in.opportunity_id).first()
    if not opp:
        raise HTTPException(status_code=404, detail="Opportunity not found")
    
    # Prevent duplicate applications
    existing = db.query(Application).filter(
        Application.user_id == current_user.id, 
        Application.opportunity_id == app_in.opportunity_id
    ).first()
    if existing:
        raise HTTPException(status_code=400, detail="You have already tracked an application for this opportunity")

    new_app = Application(
        user_id=current_user.id,
        opportunity_id=app_in.opportunity_id,
        notes=app_in.notes
    )
    db.add(new_app)
    db.commit()
    db.refresh(new_app)
    return new_app

@router.get("/", response_model=List[ApplicationResponse])
def list_my_applications(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    # Only return applications belonging to the logged-in user
    return db.query(Application).filter(Application.user_id == current_user.id).all()

@router.put("/{id}", response_model=ApplicationResponse)
def update_application_status(
    id: int, 
    app_update: ApplicationUpdate, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)
):
    # Ensure they can only update THEIR OWN application
    application = db.query(Application).filter(Application.id == id, Application.user_id == current_user.id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    
    application.status = app_update.status
    if app_update.notes is not None:
        application.notes = app_update.notes
        
    db.commit()
    db.refresh(application)
    return application