from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from app.models.v1.user.user import UserRegister
from app.api.v1.auth import auth_service
from app.models.v1.token.token_schema import Token, LoginRequest
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=Token)
def login_endpoint(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return auth_service.login_user(db, form_data.username, form_data.password)

