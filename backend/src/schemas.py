from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    username: str

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    email: EmailStr | None = None
    username: str | None = None

class UserResponse(UserBase):
    id: int
    
    class Config:
        orm_mode = True

class ProfileBase(BaseModel):
    disc_results: dict

class PodCreate(BaseModel):
    name: str
    description: str
