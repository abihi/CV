from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    # dates
    owner_id = Column(Integer, ForeignKey("profiles.id"))

    owner = relationship("Profile", back_populates="projects")
