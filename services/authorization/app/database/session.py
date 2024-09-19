from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database.config import settings

engine = create_engine(
    url=settings.DATABASE_URL_psycopg,
)

SessionFactory = sessionmaker(engine)


def get_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()
