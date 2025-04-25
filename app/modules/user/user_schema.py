from pydantic import BaseModel, EmailStr, constr

class UserBase(BaseModel):
    name: str = constr(strip_whitespace=True, min_length=1, max_length=50)
    email: EmailStr
    password: str = constr(strip_whitespace=True, min_length=8, max_length=50)
    age: int

class UserCreate(UserBase):
    pass

class UserOut(UserBase):
    id: int

    class Config:
        orm_mode = True
