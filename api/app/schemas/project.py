from typing import Optional

from pydantic import BaseModel


class ProjectBase(BaseModel):
    title: str
    description: Optional[str] = None


class ProjectCreate(ProjectBase):
    owner_id: int


class Project(ProjectBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
