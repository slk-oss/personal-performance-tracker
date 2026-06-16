from pydantic import BaseModel, EmailStr, Field

class UserCreate(BaseModel):
    email: EmailStr
    password: str = Field(min_length=6, max_length=64)

class UserRead(BaseModel):
    id: int
    email: EmailStr

    model_config = {
        "from_attributes": True
    }