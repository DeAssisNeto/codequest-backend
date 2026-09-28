import uuid
from fastapi import HTTPException, status
from app.core.security import hash_password
from app.models.models import User
from app.repositories.user_repository import UserRepository
from app.schemas.users_schema import UserCreate, UserUpdate


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    async def find_all(self) -> list[User]:
        return await self.repository.find_all()

    async def find_by_id(self, user_id: uuid.UUID) -> User:
        user = await self.repository.find_by_id(user_id)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Usuário não encontrado",
            )
        return user

    async def create(self, user_data: UserCreate) -> User:
        await self._ensure_email_available(user_data.email)
        user = User(
            **user_data.model_dump(exclude={"password"}),
            password=hash_password(user_data.password),
        )
        return await self.repository.create(user)

    async def update(self, user_id: uuid.UUID, user_data: UserUpdate) -> User:
        user = await self.find_by_id(user_id)
        data = user_data.model_dump(exclude_unset=True)

        if "email" in data and data["email"] != user.email:
            await self._ensure_email_available(data["email"])

        password = data.pop("password", None)
        if password:
            data["password"] = hash_password(password)

        return await self.repository.update(user, data)

    async def delete(self, user_id: uuid.UUID) -> None:
        user = await self.find_by_id(user_id)
        await self.repository.delete(user)

    async def _ensure_email_available(self, email: str) -> None:
        if await self.repository.find_by_email(email):
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="E-mail já cadastrado",
            )
