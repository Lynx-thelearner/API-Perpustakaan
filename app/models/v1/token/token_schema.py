from pydantic import BaseModel, EmailStr
from typing import Optional
import uuid
from sqlalchemy.dialects.postgresql import UUID

class Token(BaseModel):
    """Response ketika login sukses"""
    access_token: str
    token_type: str = "bearer"

class TokenPayload(BaseModel):
    """Isi token setelah di-decode"""
    sub: Optional[uuid.UUID] = None   # user_id 
    username: Optional[str] = None # username
    role: Optional[str] = None  # anggota/petugas
    exp: Optional[int] = None   # expiry time
    
class LoginRequest(BaseModel):
    username: str
    password: str
