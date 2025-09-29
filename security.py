import os
from datetime import datetime, timedelta
from typing import Optional, Dict, Any
import orm_models, database
from fastapi import Depends, HTTPException, status
from passlib.context import CryptContext
from jose import JWTError, jwt
from vevn import auth
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

"""Config Password Hashing"""
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

"""Buat dapatin user saat ini"""
def get_current_user(db: Session = Depends(database.get_db), token: str = Depends(oauth2_scheme)):
    payload = auth.decode_access_token(token)
    user = db.query(orm_models.User).filter(orm_models.User.id_user == int(payload.get("sub"))).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return user

def require_role(role: str):
    def role_checker(current_user: orm_models.User = Depends(get_current_user)):
        if current_user.role.value != role:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"required role: {role}"
            )
        return current_user
    return role_checker