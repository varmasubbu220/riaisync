from pydantic import BaseModel, EmailStr
from datetime import date

class UserCreate(BaseModel):
    emp_id: int  # Required Employee ID (Foreign Key)
    first_name: str
    last_name: str
    dob: date
    email: EmailStr
    phone: str | None = None
    notes: str | None = None
    password: str

class UserResponse(BaseModel):
    user_id: int
    emp_id: int
    first_name: str
    last_name: str
    dob: date
    email: EmailStr
    phone: str | None
    notes: str | None

    class Config:
        orm_mode = True


class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    dob: date | None = None
    email: EmailStr | None = None
    phone: str | None = None
    notes: str | None = None
    password: str | None = None
