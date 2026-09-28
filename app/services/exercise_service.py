import uuid
from fastapi import HTTPException, status
from app.repositories.exercise_repository import ExerciseRepository
from app.schemas.exercise_schema import ExerciseCreate
from app.models.models import Exercise


class ExerciseService:
    def __init__(self, repository: ExerciseRepository):
        self.repository = repository

    async def find_all(self) -> list[Exercise]:
        return await self.repository.find_all()

    async def find_by_id(self, exercise_id: uuid.UUID) -> Exercise:
        exercise = await self.repository.find_by_id(exercise_id)
        if exercise is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Exercício não encontrado",
            )
        return exercise

    async def create(self, exercise_data: ExerciseCreate) -> Exercise:
        return await self.repository.create(exercise_data)
