import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from sqlalchemy_utils import database_exists, create_database, drop_database

from app.database import Base
from app.tests.test_base import (
    SQLALCHEMY_DATABASE_URL as url,
    get_test_db,
    engine,
)
from app.dependency import get_db
from app import app


@pytest.fixture(scope="session", autouse=True)
def create_test_database():
    if database_exists(url):
        drop_database(url)
    create_database(url)
    Base.metadata.create_all(engine)
    app.dependency_overrides[get_db] = get_test_db
    yield
    drop_database(url)


@pytest.yield_fixture
def test_db_session():
    session = Session(bind=engine)

    yield session
    # Drop all data after each test
    for tbl in reversed(Base.metadata.sorted_tables):
        engine.execute(tbl.delete())

    session.close()


@pytest.fixture()
def client():
    with TestClient(app) as client:
        yield client
