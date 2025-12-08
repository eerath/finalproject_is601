# Tests/unit/test_change_password_logic.py

from app.operations.user import change_password
from app.models.user import User
import pytest

def test_change_password_operation(db_session):
    # Create user via model directly for operation test
    user = User(
        first_name="Unit",
        last_name="Tester",
        email="unitpw@example.com",
        username="unitpw",
        password=User.hash_password("Start1!")
    )
    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    # Try incorrect current password
    with pytest.raises(ValueError):
        change_password(db_session, user.id, type("D", (), {
            "current_password": "WrongPass",
            "new_password": "Newpass1!",
            "confirm_new_password": "Newpass1!"
        })())

    # Correct change
    data = type("D", (), {
        "current_password": "Start1!",
        "new_password": "Newpass1!",
        "confirm_new_password": "Newpass1!"
    })()
    changed_user = change_password(db_session, user.id, data)
    assert changed_user.verify_password("Newpass1!") is True
