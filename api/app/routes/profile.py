from typing import List

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from crud.profile import get_profiles, get_profile, create_profile
from schemas import Profile, ProfileCreate
from app.main import app, get_db


@app.get("/profiles/", response_model=List[Profile])
def get_all_profiles(db: Session = Depends(get_db)):
    profiles = get_profiles(db)
    return profiles


@app.get("/profiles/{profile_id}", response_model=Profile)
def get_profile_by_id(profile_id: int, db: Session = Depends(get_db)):
    db_profile = get_profile(db, profile_id=profile_id)
    if db_profile is None:
        raise HTTPException(status_code=404, detail="profile not found")
    return db_profile


@app.post("/profiles/", response_model=Profile)
def post_profile(profile: ProfileCreate, db: Session = Depends(get_db)):
    return create_profile(db=db, profile=profile)
