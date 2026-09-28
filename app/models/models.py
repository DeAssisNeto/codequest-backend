import uuid
import datetime
from sqlalchemy import String, Date, DateTime, Boolean, ForeignKey, Uuid, Enum as SAEnum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from app.models.enums import UserRole
from app.database.session import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String)
    birth_date: Mapped[datetime.date] = mapped_column(Date)
    gender: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True)
    password: Mapped[str] = mapped_column(String)
    role: Mapped[UserRole] = mapped_column(SAEnum(UserRole), default=UserRole.STUDENT)
    active: Mapped[bool] = mapped_column(Boolean, default=True)

    user_tracks: Mapped[list["UserTrack"]] = relationship(back_populates="user")
    user_exercises: Mapped[list["UserExercise"]] = relationship(back_populates="user")


class Track(Base):
    __tablename__ = "tracks"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String)
    difficulty: Mapped[str] = mapped_column(String)
    category: Mapped[str] = mapped_column(String)
    active: Mapped[bool] = mapped_column(Boolean, default=True)

    user_tracks: Mapped[list["UserTrack"]] = relationship(back_populates="track")
    track_exercises: Mapped[list["TrackExercise"]] = relationship(back_populates="track")


class Exercise(Base):
    __tablename__ = "exercises"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    title: Mapped[str] = mapped_column(String)
    statement: Mapped[str] = mapped_column(String)
    technology: Mapped[str] = mapped_column(String)
    initial_code: Mapped[str] = mapped_column(String)
    correct_answer: Mapped[str] = mapped_column(String)
    category: Mapped[str] = mapped_column(String)
    difficulty: Mapped[str] = mapped_column(String)
    active: Mapped[bool] = mapped_column(Boolean, default=True)

    track_exercises: Mapped[list["TrackExercise"]] = relationship(back_populates="exercise")
    user_exercises: Mapped[list["UserExercise"]] = relationship(back_populates="exercise")


class UserTrack(Base):
    __tablename__ = "user_tracks"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    track_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("tracks.id"))
    completed: Mapped[bool] = mapped_column(Boolean, default=False)
    completed_at: Mapped[datetime.datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    user: Mapped["User"] = relationship(back_populates="user_tracks")
    track: Mapped["Track"] = relationship(back_populates="user_tracks")


class TrackExercise(Base):
    __tablename__ = "track_exercises"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    track_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("tracks.id"))
    exercise_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("exercises.id"))
    active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True), default=datetime.datetime.utcnow
    )

    track: Mapped["Track"] = relationship(back_populates="track_exercises")
    exercise: Mapped["Exercise"] = relationship(back_populates="track_exercises")


class UserExercise(Base):
    __tablename__ = "user_exercises"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"))
    exercise_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("exercises.id"))
    answered: Mapped[bool] = mapped_column(Boolean, default=False)
    completed_at: Mapped[datetime.datetime | None] = mapped_column(
        DateTime(timezone=True), nullable=True
    )

    user: Mapped["User"] = relationship(back_populates="user_exercises")
    exercise: Mapped["Exercise"] = relationship(back_populates="user_exercises")
