from app.repositories import ExercisesRepository
from app.models import Exercises
from app.schemas.exercice import CreateExercise


class ExercisesService:
    def __init__(self, exercise_repository: ExercisesRepository, exercise_model: Exercises):
        self.exercise_repository = exercise_repository
        self.exercise_model = exercise_model

    def find_by_id(self, exercise_id):
        self.exercise_repository.find_by_id(exercise_id)

    def create(self, exercise: CreateExercise):
        if exercise.difficulty not in [1, 2, 3, 4, 5]:
            raise ValueError("Difficulty must be 1, 2, 3, 4, 5")
        exercise_model = Exercises(
            title=exercise.title,
            statement=exercise.statement,
            correct_answer=exercise.correct_answer,
            category=exercise.category,
            technology=exercise.technology,
            active=exercise.active,
            difficulty=exercise.difficulty,
        )

        self.exercise_repository.create(exercise_model)

