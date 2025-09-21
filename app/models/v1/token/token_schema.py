from pydantic import BaseModel
from typing import Optional

class Token(BaseModel):
    """Response ketika login sukses"""
    access_token: str
    token_type: str = "bearer"

class TokenPayload(BaseModel):
    """Isi token setelah di-decode"""
    sub: Optional[str] = None   # biasanya user_id atau username
    role: Optional[str] = None  # kalau mau bedain anggota/petugas
    exp: Optional[int] = None   # expiry time
