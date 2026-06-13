from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime, timezone


class Habit(SQLModel, table=True):
    __tablename__ = "habits"
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="users.id")
    title: str
    frequency: str
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )