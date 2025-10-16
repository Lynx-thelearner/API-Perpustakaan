from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import date
from enum import Enum
from sqlalchemy.dialects.postgresql import UUID
import uuid

class StatusEnum(str, Enum):
    dipinjam = "dipinjam"
    dikembalikan = "dikembalikan"
    hilang = "hilang"

class PeminjamanBase(BaseModel):
    """"Model awal peminjaman"""
    id_user: uuid.UUID
    id_petugas: uuid.UUID
    id_buku: int
    jumlah: int = Field(..., gt=0, description="Jumlah buku yang dipinjam")
    tgl_pinjam: date 
    tgl_kembali: date | None = None
    status: StatusEnum = Field(..., description="Status peminjaman")
    
class PeminjamanCreate(PeminjamanBase):
    """"Model untuk membuat data baru"""
    pass

class PeminjamanResponse(PeminjamanBase):
    """"Model untuk memberikan response"""
    id_peminjaman: int
    
    model_config = ConfigDict(from_attributes=True)
        
class PeminjamanUpdate(BaseModel):
    """"Model untuk mengupdate data"""
    id_user: Optional[uuid.UUID] = None
    id_petugas: Optional[uuid.UUID] = None
    id_buku: Optional[int] = None
    jumlah: Optional[int] = None
    tgl_pinjam: Optional[date] = None
    tgl_kembali: Optional[date] = None
    status: Optional[StatusEnum] = None
    
    model_config = ConfigDict(from_attributes=True)
    
class EnumRequestStatus(str, Enum):
    menunggu = "menunggu"
    disetujui = "disetujui"
    ditolak = "ditolak"
    
class RequestPeminjaman(BaseModel):
    """"Model untuk request peminjaman"""
    id_user: uuid.UUID
    id_buku: int
    jumlah: int = Field(..., gt=0, description="Jumlah buku yang dipinjam")
    tgl_request: date
    status: EnumRequestStatus = Field(..., description="Status request peminjaman")

class RequestPeminjamanCreate(RequestPeminjaman):
    pass

class RequestPeminjamanResponse(RequestPeminjaman):
    id_request: int
    
    model_config = ConfigDict(from_attributes=True)
    
class RequestPeminjamanUpdate(BaseModel):
    id_user: Optional[uuid.UUID] = None
    id_buku: Optional[int] = None
    jumlah: Optional[int] = None
    tgl_request: Optional[date] = None
    status: Optional[EnumRequestStatus] = None
    
    model_config = ConfigDict(from_attributes=True)