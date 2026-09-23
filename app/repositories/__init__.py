

from app.database.connection import get_session

from app.models import Exercises


class ExercisesRepository:

    def __init__(self, session: get_session()):
        self.session = session

    def find_by_id(self, exercise_id: int):
        return self.session.get(Exercises, id=exercise_id)
