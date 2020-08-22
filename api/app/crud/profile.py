from sqlalchemy.orm import Session

from app.models.profile import Profile
from app.schemas.profile import ProfileCreate


def read_profile(db: Session, profile_id: int):
    return db.query(Profile).filter(Profile.id == profile_id).first()


def read_profiles(db: Session):
    return db.query(Profile).all()


def create_profile(db: Session, profile: ProfileCreate):
    db_profile = Profile(
        name=profile.name,
        email=profile.email,
        address=profile.address,
        birthdate=profile.birthdate,
        about_me=profile.about_me,
        telephone_number=profile.telephone_number,
    )
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile
