# app/watcher/session_tracker.py

from dataclasses import dataclass
from typing import Optional
import logging
from datetime import datetime, timedelta

from app.db.connection import get_session
from app.db.queries import (
    get_or_create_app,
    get_or_create_file,
    open_session,
    close_session,
)

logger = logging.getLogger(__name__)


@dataclass
class InspectionResults:
    app_name: Optional[str]
    exe_path: Optional[str]
    file_path: Optional[str]  # None means no file detected
    file_extension: Optional[str]
    process_id: Optional[int]
    window_title: Optional[str]


class SessionTracker:
    """
    Core logic for managing file sessions.
    Decides when to open/close sessions based on detected activity.
    """

    def __init__(self, idle_timeout_seconds: int = 300):
        self.current_file_path: Optional[str] = None
        self.current_session_id: Optional[int] = None
        self.current_app_id: Optional[int] = None
        self.last_activity_time: Optional[datetime] = None
        self.idle_timeout = timedelta(seconds=idle_timeout_seconds)

    # ------------------------------------------------------------
    # PUBLIC ENTRY POINT
    # ------------------------------------------------------------
    def handle_activity(self, activity: InspectionResults):
        """
        Main entry point called by the watcher.
        """
        logger.info("Handling activity: %s", activity)

        new_path = activity.file_path

        # Case 1: No file detected → close active session
        if new_path is None:
            logger.info("No file detected. Closing any active session.")
            self._close_current_session()
            return

        # Case 2: Same file as before → do nothing
        if new_path == self.current_file_path:
            logger.info("Same file still active: %s.", new_path)
            return

        # Case 3: New file detected → close old session, open new one
        logger.info("Switching from %s to %s.", self.current_file_path, new_path)
        self._close_current_session()
        self._open_new_session(activity)

    # ------------------------------------------------------------
    # INTERNAL HELPERS
    # ------------------------------------------------------------
    def _close_current_session(self):
        if self.current_session_id is None:
            return

        logger.info("Closing session %s.", self.current_session_id)

        with get_session() as db:
            close_session(db, self.current_session_id)

        self.current_session_id = None
        self.current_file_path = None

    def _open_new_session(self, activity: InspectionResults):
        logger.info("Opening new session for file: %s.", activity.file_path)

        with get_session() as db:
            app = get_or_create_app(db, activity.app_name, activity.exe_path)
            file = get_or_create_file(db, activity.file_path, activity.extension)

            session = open_session(db, file.id, app.id)

            logger.info("New session created %s.", session.id)

            self.current_session_id = session.id
            self.current_file_path = activity.file_path
            self.current_app_id = app.id