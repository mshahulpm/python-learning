from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+psycopg2://postgres:123456@localhost:5432/python_alembic"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
