from app.config import settings 
from sqlalchemy.ext.asyncio import create_async_engine 
from sqlalchemy.ext.asyncio import async_sessionmaker

DB_URL =  f"postgresql+asyncpg://{settings.POSTGRES_USER}:{settings.POSTGRES_PASSWORD}@localhost:{settings.POSTGRES_PORT}/{settings.POSTGRES_DB}"
engine = create_async_engine(DB_URL, echo=True)

async_session = async_sessionmaker(engine, expire_on_commit=False) 

async def get_async_session():
    async with async_session() as session:
        yield session