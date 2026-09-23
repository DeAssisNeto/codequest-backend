from pydantic import BaseModel


class CreateExercise(BaseModel):
    id: str
    title: str
    statement: str
    correct_answer: str
    category: str
    technology: str
    difficulty: str
    active: bool