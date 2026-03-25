from sqlalchemy import Integer, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.db.connection import Base


class Session(Base):
    __tablename__ = "sessions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)

    file_id: Mapped[int] = mapped_column(ForeignKey("files.id"), nullable=False)
    app_id: Mapped[int] = mapped_column(ForeignKey("apps.id"), nullable=False)

    opened_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    closed_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    duration_seconds: Mapped[int | None] = mapped_column(Integer, nullable=True)

    file = relationship("File")
    app = relationship("App")

    def __repr__(self) -> str:
        return (
            f"<Session id={self.id} file_id={self.file_id} app_id={self.app_id} "
            f"opened_at={self.opened_at} closed_at={self.closed_at}>"
        )