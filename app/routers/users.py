# app/routers/users.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user import UserUpdate, UserResponse
from app.operations.user import update_user
from app.auth.dependencies import get_current_user  # you should have something like this
from app.models.user import User

router = APIRouter(prefix="/users", tags=["users"])


@router.put("/me", response_model=UserResponse)
def update_my_profile(
    user_update: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    """
    Update the logged-in user's own profile.
    """
    try:
        return update_user(db, current_user.id, user_update)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))