from sqlalchemy import Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.connection import Base


class Exercises(Base):

    __tablename__ = 'exercises'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    title: Mapped[str] = mapped_column(String, nullable=False)

    statement: Mapped[str] = mapped_column(String, nullable=False)

    correct_answer: Mapped[str] = mapped_column(String, nullable=False)

    category: Mapped[str] = mapped_column(String, nullable=False)

    technology: Mapped[str] = mapped_column(String, nullable=False)

    active: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)

    difficulty: Mapped[int] = mapped_column(Integer, nullable=False, default=0)



