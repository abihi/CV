from typing import AsyncIterable

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)


def get_test_db() -> AsyncIterable[Session]:
    sess = Session(bind=engine)
    try:
        yield sess
    finally:
        sess.close()
