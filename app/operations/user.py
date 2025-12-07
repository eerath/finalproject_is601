from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserUpdate
from typing import Optional

def update_user(db: Session, user_id: str, data: UserUpdate):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise ValueError("User not found")

    update_data = data.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(user, field, value)

    db.add(user)
    db.commit()
    db.refresh(user)

    return user