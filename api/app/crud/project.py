from sqlalchemy.orm import Session

from app.schemas.models import Project
from app.schemas.schemas import ProjectCreate


def get_project(db: Session, Project_id: int):
    return db.query(Project).filter(Project.id == Project_id).first()


def get_projects(db: Session):
    return db.query(Project).all()


def create_project(db: Session, Project: ProjectCreate):
    db_project = Project(
        title=Project.title, description=Project.description, owner_id=Project.owner_id,
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project
