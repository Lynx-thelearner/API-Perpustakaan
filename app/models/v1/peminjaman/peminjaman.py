from pydantic import BaseModel, Field
from typing import Optional
from datetime import date

class PeminjamanBase(BaseModel):
    """"Model awal peminjaman"""
    id_anggota: int
    id_petugas: int
    id_buku: int
    jumlah: int = Field(..., gt=0, description="Jumlah buku yang dipinjam")
    tgl_pinjam: date 
    tgl_kembali: date | None = None
    status: str
    
class PeminjamanCreate(PeminjamanBase):
    """"Model untuk membuat data baru"""
    pass

class PeminjamanResponse(PeminjamanBase):
    """"Model untuk memberikan response"""
    id_peminjaman: int
    
    class Config:
        from_attributes = True
        
class PeminjamanUpdate(BaseModel):
    """"Model untuk mengupdate data"""
    id_anggota: Optional[int] = None
    id_petugas: Optional[int] = None
    id_buku: Optional[int] = None
    jumlah: Optional[int] = None
    tgl_pinjam: Optional[date] = None
    tgl_kembali: Optional[date] = None
    status: Optional[str] = None
    
    class Config:
        from_attributes = True