import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database.session import get_db
from app.repositories.user_repository import UserRepository
from app.services.user_service import UserService
from app.schemas.users_schema import UserCreate, UserResponse, UserUpdate

router = APIRouter(prefix="/users", tags=["users"])


def get_user_service(db: AsyncSession = Depends(get_db)) -> UserService:
    return UserService(UserRepository(db))


@router.get("/", response_model=list[UserResponse])
async def find_all(service: UserService = Depends(get_user_service)):
    return await service.find_all()


@router.get("/{user_id}", response_model=UserResponse)
async def find_by_id(
    user_id: uuid.UUID,
    service: UserService = Depends(get_user_service),
):
    return await service.find_by_id(user_id)


@router.post("/", response_model=UserResponse, status_code=201)
async def create(
    user_data: UserCreate,
    service: UserService = Depends(get_user_service),
):
    return await service.create(user_data)


@router.patch("/{user_id}", response_model=UserResponse)
async def update(
    user_id: uuid.UUID,
    user_data: UserUpdate,
    service: UserService = Depends(get_user_service),
):
    return await service.update(user_id, user_data)


@router.delete("/{user_id}", status_code=204)
async def delete(
    user_id: uuid.UUID,
    service: UserService = Depends(get_user_service),
):
    await service.delete(user_id)
