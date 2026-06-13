from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime, timezone

class Log(SQLModel, table=True):
    __tablename__ = "logs"
    id: Optional[int] = Field(default=None, primary_key=True)
    habit_id: int = Field(foreign_key="habits.id")
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    status: bool 