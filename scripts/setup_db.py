"""
Initialize the SQLite database and create all tables.
Run this once after cloning the project or resetting the DB.
"""
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.db.connection import engine, Base

# Import models so SQLAlchemy knows about them
from app.models.app_model import App
from app.models.file_model import File
from app.models.session_model import Session


def init_db():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Database setup complete.")


if __name__ == "__main__":
    init_db()