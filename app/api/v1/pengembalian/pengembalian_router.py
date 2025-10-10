from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import database, orm_models

from app.api.v1.pengembalian import pengembalian_service
from app.models.v1.pengembalian.pengembalian import PengembalianCreate, PengembalianResponse, PengembalianUpdate
from app.models.v1.msg_response.msg import MessageResponse
from security.security import require_role, get_current_user


router = APIRouter(
    prefix="/pengembalian",
    tags=["Pengembalian"]
)

@router.post("/", response_model=PengembalianResponse, dependencies=[Depends(require_role("petugas"))])
def create_pengembalian(request: PengembalianCreate, db: Session = Depends(database.get_db)):
    return pengembalian_service.create_pengembalian(request, db)

@router.get("/", response_model=list[PengembalianResponse], dependencies=[Depends(require_role("petugas"))])
def get_all_pengembalian(db: Session = Depends(database.get_db)):
    return pengembalian_service.get_all_pengembalian(db)

@router.get("/{id_pengembalian}", response_model=PengembalianResponse, dependencies=[Depends(require_role("petugas"))])
def get_pengembalian(id_pengembalian: int, db: Session = Depends(database.get_db)):
    return pengembalian_service.get_pengembalian(id_pengembalian, db)

@router.patch("/{id_pengembalian}", response_model=PengembalianResponse, dependencies=[Depends(require_role("petugas"))])
def update_pengembalian(id_pengembalian: int, request: PengembalianUpdate, db: Session = Depends(database.get_db)):
    return pengembalian_service.update_pengembalian(id_pengembalian, request, db)

@router.delete("/{id_pengembalian}", response_model=MessageResponse, dependencies=[Depends(require_role("petugas"))])
def delete_pengembalian(id_pengembalian: int, db: Session = Depends(database.get_db)):
    return pengembalian_service.delete_pengembalian(id_pengembalian, db)