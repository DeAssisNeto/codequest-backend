from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from app.database.config import settings

engine = create_engine(
    settings.DATABASE_URL
)


SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


class Base(DeclarativeBase):
    pass


def get_session():
    with SessionLocal() as session:
        yield session
