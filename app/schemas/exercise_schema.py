import uuid
from pydantic import BaseModel


class ExerciseBase(BaseModel):
    title: str
    statement: str
    technology: str
    initial_code: str
    correct_answer: str
    category: str
    difficulty: str


class ExerciseUpdate(BaseModel):
    title: str | None = None
    statement: str | None = None
    technology: str | None = None
    initial_code: str | None = None
    correct_answer: str | None = None
    category: str | None = None
    difficulty: str | None = None
    active: bool | None = None


class ExerciseCreate(ExerciseBase):
    pass


class ExerciseResponse(ExerciseBase):
    id: uuid.UUID
    active: bool

    model_config = {"from_attributes": True}
