

from app.database.connection import get_session

from app.models import Exercises

from app.schemas.exercice import CreateExercise


class ExercisesRepository:

    def __init__(self, session: get_session()):
        self.session = session

    def find_by_id(self, exercise_id: int):
        return self.session.get(Exercises, id=exercise_id)

    def create(self, exercise: Exercises):
        self.session.add(exercise)

