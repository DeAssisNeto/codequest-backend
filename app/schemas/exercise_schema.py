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


class ExerciseCreate(ExerciseBase):
    pass


class ExerciseResponse(ExerciseBase):
    id: uuid.UUID
    active: bool

    model_config = {"from_attributes": True}
