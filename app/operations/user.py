from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserUpdate, PasswordUpdate
from typing import Optional

# Verify user exists in database and update
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

# Function for changing password
def change_password(db: Session, user_id: str, data: PasswordUpdate):
    """
    Verify current password matches.
    Then, hash and save the new password.
    """
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise ValueError("User not found")
    
    if not user.verify_password(data.current_password):
        raise ValueError("Current password is incorrect")
    
    hashed = User.hash_password(data.new_password)
    user.password = hashed

    db.add(user)
    db.commit()
    db.refresh(user)
    return user