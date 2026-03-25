from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from app.db.connection import Base


class App(Base):
    __tablename__ = "apps"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    exe_path: Mapped[str] = mapped_column(String, nullable=False)

    def __repr__(self) -> str:
        return f"<App id={self.id} name={self.name} exe={self.exe_path}>"