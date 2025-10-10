from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import database

from app.api.v1.kategori import kategori_service
from app.models.v1.kategori.kategori import KategoriCreate, KategoriResponse, KategoriUpdate
from app.models.v1.msg_response.msg import MessageResponse 
from security.security import require_role, get_current_user


router = APIRouter(
    prefix="/kategori",
    tags=["kategori"]
)

@router.post("/", response_model=KategoriResponse, dependencies=[Depends(require_role("petugas"))])
def create_kategori(request: KategoriCreate, db: Session = Depends(database.get_db)):
    return kategori_service.create_kategori(request, db)

@router.get("/", response_model=list[KategoriResponse])
def get_all_kategori(db: Session = Depends(database.get_db)):
    return kategori_service.get_all_kategori(db)

@router.get("/{id_kategori}", response_model=KategoriResponse)
def get_kategori(id_kategori: int, db: Session = Depends(database.get_db)):
    return kategori_service.get_kategori(id_kategori, db)

@router.patch("/{id_kategori}", response_model=KategoriResponse, dependencies=[Depends(require_role("petugas"))])
def update_kategori(id_kategori: int, request: KategoriUpdate, db: Session = Depends(database.get_db)):
    return kategori_service.update_kategori(id_kategori, request, db)

@router.delete("/{id_kategori}", response_model=MessageResponse, dependencies=[Depends(require_role("petugas"))])
def delete_kategori(id_kategori: int, db: Session = Depends(database.get_db)):
    return kategori_service.delete_kategori(id_kategori, db)