from app.repositories import ExercisesRepository

class ExercisesService:
    def __init__(self, exercise_repository: ExercisesRepository):
        self.exercise_repository = exercise_repository

    def find_by_id(self, exercise):
        self.exercise_repository.find_by_id(exercise)

