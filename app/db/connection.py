import os
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


# ------------------------------------------------------------
# Base class for all ORM models
# ------------------------------------------------------------
class Base(DeclarativeBase):
    pass


# ------------------------------------------------------------
# Database path and engine
# ------------------------------------------------------------
def get_database_url() -> str:
    """
    Returns the SQLite database URL.
    Stored in /data/file_log.db relative to project root.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    db_path = os.path.join(base_dir, "data", "file_log.db")
    return f"sqlite:///{db_path}"


engine = create_engine(
    get_database_url(), echo=False, future=True  # Set to True if you want SQL logs
)


# ------------------------------------------------------------
# Session factory
# ------------------------------------------------------------
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)


# ------------------------------------------------------------
# Dependency-style session generator
# (Even though you're not using FastAPI, this pattern is clean)
# ------------------------------------------------------------
@contextmanager
def get_session():
    """
    Context-managed session generator.
    Usage:
        with get_session() as db:
            db.query(...)
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
