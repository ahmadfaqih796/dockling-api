from sqlalchemy.orm import Session
from app.models.user_model import User
from app.modules.user.user_schema import UserCreate, UserBase
from app.services import base_service

def create_user(db: Session, user: UserCreate):
    return base_service.create(db, User, user)

def get_users(db: Session):
    return base_service.get_all(db, User)

def get_user_by_id(db: Session, user_id: int):
    return base_service.get_by_id(db, User, user_id)

def update_user(db: Session, user_id: int, user_update: UserBase):
    user = get_user_by_id(db, user_id)
    if not user:
        return None
    return base_service.update(db, user, user_update)

def delete_user(db: Session, user_id: int):
    user = get_user_by_id(db, user_id)
    if not user:
        return None
    base_service.delete(db, user)
    return user
