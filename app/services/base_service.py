from sqlalchemy.orm import Session

def create(db: Session, model_class, schema_data):
    db_obj = model_class(**schema_data.dict())
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_all(db: Session, model_class):
    return db.query(model_class).all()

def get_by_id(db: Session, model_class, id: int):
    return db.query(model_class).filter(model_class.id == id).first()

def update(db: Session, db_obj, update_data):
    for key, value in update_data.dict(exclude_unset=True).items():
        setattr(db_obj, key, value)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete(db: Session, db_obj):
    db.delete(db_obj)
    db.commit()
