from pydantic import BaseModel, ConfigDict
from typing import Optional

class KategoriBase(BaseModel):
    nama_kategori: str
    
class KategoriCreate(KategoriBase):
    pass

class KategoriResponse(KategoriBase):
    id_kategori: int
    
    model_config = ConfigDict(from_attributes=True)
        
class KategoriUpdate(BaseModel):
    nama_kategori: Optional[str] = None
    
    model_config = ConfigDict(from_attributes=True)