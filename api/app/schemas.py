from typing import List, Optional

from pydantic import BaseModel


class ProjectBase(BaseModel):
    title: str
    description: Optional[str] = None


class ProjectCreate(ProjectBase):
    pass


class Project(ProjectBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


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
