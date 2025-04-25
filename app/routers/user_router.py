from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate, UserOut
from app.services import user_service
from app.core.deps import get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    if user.name == "admin":
        raise HTTPException(status_code=400, detail="Username 'admin' is not allowed")
    return user_service.create_user(db, user)

@router.get("/", response_model=list[UserOut])
def read_users(db: Session = Depends(get_db)):
    return user_service.get_users(db)
