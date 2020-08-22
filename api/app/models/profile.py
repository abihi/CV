from sqlalchemy import Column, Integer, String
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
