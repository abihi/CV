from fastapi import FastAPI
from app.database import engine, Base

from app.models.profile import Profile
from app.models.project import Project

Base.metadata.create_all(bind=engine)

app = FastAPI()


from app.routes import profile
from app.routes import project
