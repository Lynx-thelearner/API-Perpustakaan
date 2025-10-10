from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from orm_models import User
from app.models.v1.token.token_schema import Token
from security.security import verify_password
from security.auth import create_access_token

def aunthenticate_user(db: Session, username: str, password: str) -> User:
    """Authenticate User by username and Password."""
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Incorrect username or password"
        )
    return user


def login_user(db: Session, username: str, password: str) -> Token:
    """Login User and return access token."""
    user = aunthenticate_user(db, username, password)

    access_token = create_access_token(
        subject=str(user.id_user),
        extra={
            "username": user.username,
            "role": user.role.value
            } #ngambil role dari user (Table databse Enum)
    )

    return Token(access_token=access_token, token_type="bearer")