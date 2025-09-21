import os
from datetime import datetime, timedelta
from typing import Optional, Dict, Any

from passlib.context import CryptContext
from jose import JWTError, jwt

"""Config Password Hashing"""
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

"""Config JWT Token"""
SECRET_KEY = os.getenv("SECRET_KEY", "Nqeam_mDJkMWgW9pGRfk3hxN7fc5ukxTxunQRpDY4dA")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
ACESSS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACESSS_TOKEN_EXPIRE_MINUTES", "60"))

"""Membuat Access Token"""
def create_access_token(subject:str , expires_delta: Optional[timedelta] = None, extra: Optional[dict[str, Any]] = None) -> str:
    now = datetime.utcnow()
    if expires_delta is None:
        expires_delta = timedelta(minutes=ACESSS_TOKEN_EXPIRE_MINUTES)
    expire = now + expires_delta
    
    to_encode: Dict[str, Any] = {"sub": subject, "iat": now, "exp": expire}
    if extra:
        to_encode.update(extra)
        
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

"""Decode dan verifikasi Access Token"""
def decode_access_token(token: str) -> Dict[str, Any]:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError as e:
        raise