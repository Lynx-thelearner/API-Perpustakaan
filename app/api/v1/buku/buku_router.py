from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import database

from app.api.v1.buku import buku_service
from app.models.v1.buku.buku import BukuCreate, BukuResponse, BukuUpdate
from app.models.v1.msg_response import msg
from security.security import require_role, get_current_user

router = APIRouter(
    prefix="/buku",
    tags=["Buku"]
)

@router.post("/", response_model=BukuResponse, dependencies=[Depends(require_role("petugas"))])
def create_buku(request: BukuCreate, db: Session = Depends(database.get_db)):
    return buku_service.create_buku(request, db)

@router.get("/", response_model=list[BukuResponse])
def get_all_buku(db: Session = Depends(database.get_db)):
    return buku_service.get_all_buku(db)

@router.get("/{id_buku}", response_model=BukuResponse)
def get_buku(id_buku: int, db: Session = Depends(database.get_db)):
    return buku_service.get_buku(id_buku, db)

@router.patch("/{id_buku}", response_model=BukuResponse, dependencies=[Depends(require_role("petugas"))])
def update_buku(id_buku: int, request: BukuUpdate, db: Session = Depends(database.get_db)):
    return buku_service.update_buku(id_buku, request, db)

@router.delete("/{id_buku}", response_model=msg.MessageResponse, dependencies=[Depends(require_role("petugas"))])
def delete_buku(id_buku: int, db: Session = Depends(database.get_db)):
    return buku_service.delete_buku(id_buku, db)