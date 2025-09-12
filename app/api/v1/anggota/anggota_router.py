from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import database

from app.api.v1.anggota import anggota_service  
from app.models.v1.anggota.anggota import AnggotaCreate, AnggotaResponse, AnggotaUpdate
from app.models.v1.msg_response import msg 

router = APIRouter(
    prefix="/anggota",
    tags=["Anggota"]
)

@router.post("/", response_model=AnggotaResponse)
def create_anggota(request: AnggotaCreate, db: Session = Depends(database.get_db)):
    return anggota_service.create_anggota(request, db)

@router.get("/", response_model=list[AnggotaResponse])
def get_all_anggota(db: Session = Depends(database.get_db)):
    return anggota_service.get_all_anggota(db)

@router.get("/{id_anggota}", response_model=AnggotaResponse)
def get_anggota(id_anggota: int, db: Session = Depends(database.get_db)):
    return anggota_service.get_anggota(id_anggota, db)

@router.put("/{id_anggota}", response_model=AnggotaResponse)
def update_anggota(id_anggota: int, request: AnggotaUpdate, db: Session = Depends(database.get_db)):
    return anggota_service.update_anggota(id_anggota, request, db)

