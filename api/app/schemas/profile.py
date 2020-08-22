from typing import List

from pydantic import BaseModel

from app.schemas.project import Project


class ProfileBase(BaseModel):
    name: str
    email: str
    address: str
    # Change to Date datatype
    birthdate: str
    about_me: str
    telephone_number: str


class ProfileCreate(ProfileBase):
    pass


class Profile(ProfileBase):
    id: int
    projects: List[Project] = []

    class Config:
        orm_mode = True
