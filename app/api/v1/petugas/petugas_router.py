from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import database

from app.api.v1.petugas import petugas_service  
from app.models.v1.petugas.petugas import PetugasCreate, PetugasResponse, PetugasUpdate
from app.models.v1.msg_response.msg import MessageResponse

router = APIRouter(
    prefix="/petugas",
    tags=["Petugas"]
)

@router.post("/", response_model=PetugasResponse)
def create_petugas(request: PetugasCreate, db: Session = Depends(database.get_db)):
    return petugas_service.create_petugas(request, db)

@router.get("/", response_model=list[PetugasResponse])
def get_all_petugas(db: Session = Depends(database.get_db)):
    return petugas_service.get_all_petugas(db)

@router.get("/{id_petugas}", response_model=PetugasResponse)
def get_petugas(id_petugas: int, db: Session = Depends(database.get_db)):
    return petugas_service.get_petugas(id_petugas, db)

@router.put("/{id_petugas}", response_model=PetugasResponse)
def update_petugas(id_petugas: int, request: PetugasUpdate, db: Session = Depends(database.get_db)):
    return petugas_service.update_petugas(id_petugas, request, db)

@router.delete("/{id_petugas}", response_model=MessageResponse)
def delete_petugas(id_petugas: int, db: Session = Depends(database.get_db)):
    return petugas_service.delete_petugas(id_petugas, db)
