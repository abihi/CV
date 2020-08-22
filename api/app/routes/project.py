from typing import List

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from app.crud.project import read_projects, read_project, create_project
from app.schemas.project import Project, ProjectCreate
from app.dependency import get_db
from app import app


@app.get("/projects", response_model=List[Project])
def get_projects(db: Session = Depends(get_db)):
    projects = read_projects(db)
    return projects


@app.get("/projects/{project_id}", response_model=Project)
def get_project(project_id: int, db: Session = Depends(get_db)):
    db_project = read_project(db, project_id=project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="project not found")
    return db_project


@app.post("/projects", response_model=Project)
def post_project(project: ProjectCreate, db: Session = Depends(get_db)):
    return create_project(db=db, project=project)
