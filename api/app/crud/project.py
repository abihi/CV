from sqlalchemy.orm import Session

from app.models.project import Project
from app.schemas.project import ProjectCreate


def read_project(db: Session, project_id: int):
    return db.query(Project).filter(Project.id == project_id).first()


def read_projects(db: Session):
    return db.query(Project).all()


def create_project(db: Session, project: ProjectCreate):
    db_project = Project(
        title=project.title, description=project.description, owner_id=project.owner_id,
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project
