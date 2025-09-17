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

class PetugasBase(BaseModel):
    """Model awal petugas"""
    nama: str = Field(..., description="Nama lengkap petugas")
    alamat: str = Field(..., description="Alamat lengkap petugas")
    no_telp: Phone = Field(..., description="Nomor telepon petugas")
    email: EmailStr = Field(..., examples=["user@gmail.com"], description="Alamat email petugas")

class PetugasCreate(PetugasBase):
    """Model untuk membuat data baru"""
    password: str = Field(..., description="Masukan Password (Minimum 8 karakter)", min_length=8)

class PetugasResponse(PetugasBase):
    """Model untuk memberikan response"""
    id_petugas: int

    class Config:
        from_attributes = True

class PetugasUpdate(BaseModel):
    nama: Optional[str] = None
    alamat: Optional[str] = None
    no_telp: Optional[Phone] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = Field(None, min_length=8)

    class Config:
        from_attributes = True
