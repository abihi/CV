from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/profiles/", response_model=List[schemas.Profile])
def get_all_profiles(db: Session = Depends(get_db)):
    profiles = crud.get_profiles(db)
    return profiles


@app.get("/profiles/{profile_id}", response_model=schemas.Profile)
def get_profile(profile_id: int, db: Session = Depends(get_db)):
    db_profile = crud.get_profile(db, profile_id=profile_id)
    if db_profile is None:
        raise HTTPException(status_code=404, detail="profile not found")
    return db_profile


@app.post("/profiles/", response_model=schemas.Profile)
def create_profile(profile: schemas.ProfileCreate, db: Session = Depends(get_db)):
    return crud.create_profile(db=db, profile=profile)
