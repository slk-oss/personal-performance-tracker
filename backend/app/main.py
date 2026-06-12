from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import engine
from sqlmodel import SQLModel
from app.models.user import User


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Приложение запускается: создаем таблицы...")
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    yield
    print("Приложение завершается: закрываем соединение с базой данных...")
    await engine.dispose()

app = FastAPI(lifespan=lifespan)
@app.get("/health")
async def get_health_status():
    return {"status": "ok"}
