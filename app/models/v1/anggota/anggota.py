from pydantic import BaseModel, Field, EmailStr, StringConstraints
from typing import Optional, Annotated

# Tipe data untuk nomor telepon
Phone = Annotated[
    str,
    StringConstraints(
        pattern=r"^(?:\+62|0)8[1-9][0-9]{6,11}$",
        min_length=10,
        max_length=15,
    )
]

class AnggotaBase(BaseModel):
    """Model Awal"""
    nama: str = Field(..., description="Nama lengkap anggota")
    alamat: str = Field(..., description="Alamat lengkap anggota")
    no_telp: Phone = Field(..., description="Nomor telepon anggota")
    email: EmailStr = Field(..., examples=["user@example.com"], description="Alamat email anggota")

class AnggotaCreate(AnggotaBase):
    """Model untuk membuat data baru"""
    pass

class AnggotaResponse(AnggotaBase):
    """Model untuk memberikan response"""
    id_anggota: int
    
    class Config:
        from_attributes = True

class AnggotaUpdate(BaseModel):
    """Model untuk mengupdate data"""
    nama: Optional[str] = None
    alamat: Optional[str] = None
    no_telp: Optional[Phone] = None
    email: Optional[EmailStr] = None
    
    class Config:
        from_attributes = True
