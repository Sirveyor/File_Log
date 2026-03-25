from datetime import datetime
from sqlalchemy import select, update
from sqlalchemy.orm import Session

from app.models.app_model import App
from app.models.file_model import File
from app.models.session_model import Session as FileSession


# ------------------------------------------------------------
# APP QUERIES
# ------------------------------------------------------------
def get_or_create_app(db: Session, name: str, exe_path: str) -> App:
    stmt = select(App).where(App.name == name, App.exe_path == exe_path)
    app = db.scalar(stmt)

    if app:
        return app

    app = App(name=name, exe_path=exe_path)
    db.add(app)
    db.commit()
    db.refresh(app)
    return app


# ------------------------------------------------------------
# FILE QUERIES
# ------------------------------------------------------------
def get_or_create_file(db: Session, path: str, extension: str | None) -> File:
    stmt = select(File).where(File.path == path)
    file = db.scalar(stmt)

    if file:
        return file

    file = File(path=path, extension=extension)
    db.add(file)
    db.commit()
    db.refresh(file)
    return file


# ------------------------------------------------------------
# SESSION QUERIES
# ------------------------------------------------------------
def open_session(db: Session, file_id: int, app_id: int) -> FileSession:
    """
    Creates a new session for a file/app pair.
    """
    session = FileSession(
        file_id=file_id,
        app_id=app_id,
        opened_at=datetime.now(),
        closed_at=None,
        duration_seconds=None
    )
    db.add(session)
    db.commit()
    db.refresh(session)
    return session


def close_session(db: Session, session_id: int) -> FileSession:
    """
    Closes an existing session by setting closed_at and duration.
    """
    stmt = select(FileSession).where(FileSession.id == session_id)
    session = db.scalar(stmt)

    if not session or session.closed_at is not None:
        return session  # Already closed or not found

    session.closed_at = datetime.now()
    session.duration_seconds = int(
        (session.closed_at - session.opened_at).total_seconds()
    )

    db.commit()
    db.refresh(session)
    return session


def get_active_session(db: Session) -> FileSession | None:
    """
    Returns the currently open session (if any).
    """
    stmt = select(FileSession).where(FileSession.closed_at.is_(None))
    return db.scalar(stmt)


def close_active_session(db: Session) -> FileSession | None:
    """
    Convenience helper: closes whichever session is currently open.
    """
    active = get_active_session(db)
    if not active:
        return None

    return close_session(db, active.id)