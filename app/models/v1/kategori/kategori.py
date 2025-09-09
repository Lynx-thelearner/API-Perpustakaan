from pydantic import BaseModel
from typing import Optional

class KategoriBase(BaseModel):
    nama_kategori: str
    
class KategoriCreate(KategoriBase):
    pass

class KategoriResponse(KategoriBase):
    id_kategori: int
    
    class Config:
        from_attributes = True
        
class KategoriUpdate(BaseModel):
    nama_kategori: Optional[str] = None
    
    class Config:
        from_attributes = True