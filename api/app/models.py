from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, index=True)
    address = Column(String)
    # Change to Date datatype
    birthdate = Column(String)
    about_me = Column(String)
    telephone_number = Column(String)

    projects = relationship("Project", back_populates="owner")


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    # dates
    owner_id = Column(Integer, ForeignKey("profiles.id"))

    owner = relationship("Profile", back_populates="projects")
