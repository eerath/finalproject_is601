# app/routers/users.py

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.user import UserUpdate, UserResponse, PasswordUpdate
from app.operations.user import update_user, change_password
from app.auth.dependencies import get_current_user  
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
    
@router.put("/me/password", status_code=status.HTTP_200_OK)
def update_my_password(
    pw_update: PasswordUpdate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user),
):
    """
    Change the logged-in user's password.
    Returns 200 on success, 400/404 on failure.
    """
    try:
        # current_user may be a Pydantic UserResponse or a SQLAlchemy User
        user_id = getattr(current_user, "id", current_user)
        user = change_password(db, user_id, pw_update)
        return {"message": "Password updated successfully"}
    except ValueError as e:
        # current password wrong or user not found
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))