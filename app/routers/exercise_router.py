import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.repositories.exercise_repository import ExerciseRepository
from app.services.exercise_service import ExerciseService
from app.schemas.exercise_schema import ExerciseCreate, ExerciseResponse

router = APIRouter(prefix="/exercises", tags=["exercises"])


def get_exercise_service(db: AsyncSession = Depends(get_db)) -> ExerciseService:
    repository = ExerciseRepository(db)
    return ExerciseService(repository)


@router.get("/", response_model=list[ExerciseResponse])
async def find_all(service: ExerciseService = Depends(get_exercise_service)):
    return await service.find_all()


@router.get("/{exercise_id}", response_model=ExerciseResponse)
async def find_by_id(
    exercise_id: uuid.UUID,
    service: ExerciseService = Depends(get_exercise_service),
):
    return await service.find_by_id(exercise_id)


@router.post("/", response_model=ExerciseResponse, status_code=201)
async def create(
    exercise_data: ExerciseCreate,
    service: ExerciseService = Depends(get_exercise_service),
):
    return await service.create(exercise_data)
