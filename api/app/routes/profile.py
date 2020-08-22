from typing import List

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.profile import read_profiles, read_profile, create_profile
from app.schemas.profile import Profile, ProfileCreate
from app.dependency import get_db
from app import app


@app.get("/profiles", response_model=List[Profile])
def get_profiles(db: Session = Depends(get_db)):
    profiles = read_profiles(db)
    return profiles


@app.get("/profiles/{profile_id}", response_model=Profile)
def get_profile(profile_id: int, db: Session = Depends(get_db)):
    db_profile = read_profile(db, profile_id=profile_id)
    if db_profile is None:
        raise HTTPException(status_code=404, detail="profile not found")
    return db_profile


@app.post("/profiles", response_model=Profile)
def post_profile(profile: ProfileCreate, db: Session = Depends(get_db)):
    return create_profile(db=db, profile=profile)
