from pydantic import BaseModel


class CreateExercise(BaseModel):
    title: str
    statement: str
    correct_answer: str
    category: str
    technology: str
    difficulty: int
    active: bool
