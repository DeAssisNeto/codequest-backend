import uuid
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.models import Exercise
from app.schemas.exercise_schema import ExerciseCreate, ExerciseUpdate


class ExerciseRepository:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def find_all(self) -> list[Exercise]:
        result = await self.db.execute(select(Exercise))
        return list(result.scalars().all())

    async def find_by_id(self, exercise_id: uuid.UUID) -> Exercise | None:
        result = await self.db.execute(
            select(Exercise).where(Exercise.id == exercise_id)
        )
        return result.scalar_one_or_none()

    async def create(self, exercise_data: ExerciseCreate) -> Exercise:
        exercise = Exercise(**exercise_data.model_dump())
        self.db.add(exercise)
        await self.db.commit()
        await self.db.refresh(exercise)
        return exercise

    async def delete(self, exercicio: Exercise) -> None:
        exercicio.active = False
        await self.db.commit()


    async def update(self, exercise: Exercise, exercise_data: ExerciseUpdate) -> Exercise:
        # exclude_unset=True: só altera os campos que o cliente realmente enviou
        for field, value in exercise_data.model_dump(exclude_unset=True).items():
            setattr(exercise, field, value)
        await self.db.commit()
        await self.db.refresh(exercise)
        return exercise
