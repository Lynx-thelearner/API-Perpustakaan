from pydantic import BaseModel
from typing import Optional
from datetime import date
from decimal import Decimal

class PengembalianBase(BaseModel):
    """"Model awal pengembalian"""
    id_peminjaman: int
    tgl_kembali: date
    denda: Decimal
    
class PengembalianCreate(PengembalianBase):
    """Model untuk membuat data baru"""
    pass

class PengembalianResponse(PengembalianBase):
    """"Model untuk memberikan response"""
    id_pengembalian: int
    
    class Config:
        from_attributes = True
        
class PengembalianUpdate(BaseModel):
    """"Model untuk mengupdate data"""
    id_peminjaman: Optional[int] = None
    tgl_kembali: Optional[date] = None
    denda: Optional[Decimal] = None
    
    class Config:
        from_attributes = True