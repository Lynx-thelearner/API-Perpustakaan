from pydantic import BaseModel, Field, EmailStr, StringConstraints, ConfigDict
from typing import Optional, Annotated
from enum import Enum
from sqlalchemy.dialects.postgresql import UUID
import uuid


# Tipe data untuk nomor telepon
Phone = Annotated[
    str,
    StringConstraints(
        pattern=r"^(?:\+62|0)8[1-9][0-9]{6,11}$",
        min_length=10,
        max_length=15,
    )
]

class RoleEnum(str, Enum):
    anggota = "anggota"
    petugas = "petugas"

class UserBase(BaseModel):
    """Model Awal"""
    nama: str = Field(..., description="Nama lengkap user")
    username: str = Field(..., description="Username unik untuk login")
    alamat: str = Field(..., description="Alamat lengkap user")
    no_telp: Phone = Field(..., description="Nomor telepon user")
    email: EmailStr = Field(..., examples=["user@example.com"], description="Alamat email user")
    role: RoleEnum = Field(..., description="Role user, bisa 'anggota' atau 'petugas'")
    

class UserCreate(UserBase):
    """Model untuk membuat data baru"""
    password: str = Field(..., min_length=8, max_length=72, description="Password user (minimal 8 karakter)")

class UserResponse(UserBase):
    """Model untuk memberikan response"""
    id_user: uuid.UUID
    
    model_config = ConfigDict(from_attributes=True)

class UserUpdate(BaseModel):
    """Model untuk mengupdate data"""
    nama: Optional[str] = None
    username: Optional[str] = None
    alamat: Optional[str] = None
    no_telp: Optional[Phone] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(None, min_length=8)
    role: Optional[RoleEnum] = None
    
class UserRegister(BaseModel):
    nama: str = Field(..., description="Nama lengkap")
    username: str = Field(..., description="Username unik untuk login")
    alamat: str = Field(..., description="Alamat Pengguna")
    no_telp: Phone = Field(..., description="Nomor Telpon")
    email: EmailStr = Field(..., examples=["user@example.com"], description="Alamat Email anda")
    password: str = Field(..., min_length=8, description="Password User (Minimal 8 Karakter)")