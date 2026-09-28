from fastapi import FastAPI
from app.database.session import engine, Base


from app.routers.exercise_router import router as exercise_router
from app.routers.user_router import router as user_router

app = FastAPI()

app.include_router(exercise_router)
app.include_router(user_router)


@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
