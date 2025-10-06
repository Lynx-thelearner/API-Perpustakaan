from pydantic import BaseModel, Field, ConfigDict
from typing import Optional

class BukuBase(BaseModel):
    judul: str = Field(..., description="Judul buku")
    pengarang: str = Field(..., description="Nama pengarang buku")
    penerbit: str = Field(..., description="Nama penerbit buku")
    tahun_terbit: int = Field(..., description="Tahun terbit buku")
    stok: int = Field(..., ge=0, description="Stok buku yang tersedia")
    id_kategori: int
    
class BukuCreate(BukuBase):
    pass

class BukuResponse(BukuBase):
    id_buku: int
    
    model_config = ConfigDict(from_attributes=True)
        
class BukuUpdate(BaseModel):
    judul: Optional[str] = None
    pengarang: Optional[str] = None
    penerbit: Optional[str] = None
    tahun_terbit: Optional[int] = None
    stok: Optional[int] = None
    id_kategori: Optional[int] = None
    
    model_config = ConfigDict(from_attributes=True)