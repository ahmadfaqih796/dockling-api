from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.modules.user.user_schema import UserCreate, UserOut, UserBase
from app.modules.user import user_service
from app.core.deps import get_db

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    if user.name.lower() == "admin":
        raise HTTPException(status_code=400, detail="Username 'admin' is not allowed")
    return user_service.create_user(db, user)

@router.get("/", response_model=list[UserOut])
def read_users(db: Session = Depends(get_db)):
    return user_service.get_users(db)

@router.get("/{user_id}", response_model=UserOut)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = user_service.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put("/{user_id}", response_model=UserOut)
def update_user(user_id: int, user_update: UserBase, db: Session = Depends(get_db)):
    user = user_service.update_user(db, user_id, user_update)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.delete("/{user_id}", response_model=UserOut)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = user_service.delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
