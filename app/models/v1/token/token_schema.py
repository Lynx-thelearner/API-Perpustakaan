from pydantic import BaseModel, EmailStr
from typing import Optional

class Token(BaseModel):
    """Response ketika login sukses"""
    access_token: str
    token_type: str = "bearer"

class TokenPayload(BaseModel):
    """Isi token setelah di-decode"""
    sub: Optional[str] = None   # user_id atau email
    username: Optional[str] = None # username
    role: Optional[str] = None  # anggota/petugas
    exp: Optional[int] = None   # expiry time
    
class LoginRequest(BaseModel):
    email: EmailStr
    password: str
