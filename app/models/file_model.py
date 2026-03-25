from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.db.connection import Base


class File(Base):
    __tablename__ = "files"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    path: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    extension: Mapped[str | None] = mapped_column(String, nullable=True)

    def __repr__(self) -> str:
        return f"<File id={self.id} path={self.path}>"