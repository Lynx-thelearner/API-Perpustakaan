from pydantic import BaseModel, field
from typing import Optional

class BukuBase(BaseModel):
    judul: str = field(..., description="Judul buku")
    pengarang: str = field(..., description="Nama pengarang buku")
    penerbit: str = field(..., description="Nama penerbit buku")
    tahun_terbit: int = field(..., description="Tahun terbit buku")
    stok: int = field(..., ge=0, description="Stok buku yang tersedia")
    id_kategori: int
    
class BukuCreate(BukuBase):
    pass

class BukuResponse(BukuBase):
    id_buku: int
    
    class Config:
        from_attributes = True
        
class BukuUpdate(BaseModel):
    judul: Optional[str] = None
    pengarang: Optional[str] = None
    penerbit: Optional[str] = None
    tahun_terbit: Optional[int] = None
    stok: Optional[int] = None
    id_kategori: Optional[int] = None
    
    class Config:
        from_attributes = True