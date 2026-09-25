import uuid

from sqlalchemy.orm import Session

from app.models import Exercises

from app.schemas.exercice import CreateExercise


class ExercisesRepository:

    def __init__(self, session: Session):
        self.session = session

    def find_by_id(self, exercise_id: uuid.UUID):
        return self.session.get(Exercises, id=exercise_id)

    def create(self, exercise: Exercises):
        self.session.add(exercise)

