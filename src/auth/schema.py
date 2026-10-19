from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class SchemaRegisterRequest(BaseModel):
    name: str = Field(..., min_length=3)
    email: EmailStr
    password: str = Field(..., min_length=6)


class SchemaLoginRequest(BaseModel):
    email: EmailStr
    password: str


class SchemaUserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str
    email: str
    created_at: datetime


class SchemaRegisterReturn(BaseModel):
    name: str
