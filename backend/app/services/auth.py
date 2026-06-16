from app.models.user import User
from app.schemas.user import UserCreate
from app.services.security import hash_password
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from fastapi import HTTPException

async def register_user(user_data: UserCreate, session: AsyncSession) -> User:
    presence_check = select(User).where(User.email == user_data.email)
    result = await session.exec(presence_check)
    check_user = result.first() 
    if check_user:
        raise HTTPException(status_code=400, detail="Такой пользователь уже зарегистрирован")

    new_user = User(email=user_data.email, password_hash=hash_password(user_data.password))
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user