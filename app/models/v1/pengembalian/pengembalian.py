from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import date
from decimal import Decimal

class PengembalianBase(BaseModel):
    """"Model awal pengembalian"""
    id_peminjaman: int
    tgl_kembali: date
    denda: float
    
class PengembalianCreate(PengembalianBase):
    """Model untuk membuat data baru"""
    pass

class PengembalianResponse(PengembalianBase):
    """"Model untuk memberikan response"""
    id_pengembalian: int
    
    model_config = ConfigDict(from_attributes=True)
        
class PengembalianUpdate(BaseModel):
    """"Model untuk mengupdate data"""
    id_peminjaman: Optional[int] = None
    tgl_kembali: Optional[date] = None
    denda: Optional[float] = None
    
    model_config = ConfigDict(from_attributes=True)