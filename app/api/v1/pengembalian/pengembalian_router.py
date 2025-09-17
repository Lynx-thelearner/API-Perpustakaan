from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import database, orm_models

from app.api.v1.pengembalian import pengembalian_service
from app.models.v1.pengembalian.pengembalian import PengembalianCreate, PengembalianResponse, PengembalianUpdate
from app.models.v1.msg_response.msg import MessageResponse

router = APIRouter(
    prefix="/pengembalian",
    tags=["Pengembalian"]
)

@router.post("/", response_model=PengembalianResponse)
def create_pengembalian(request: PengembalianCreate, db: Session = Depends(database.get_db)):
    return pengembalian_service.create_pengembalian(request, db)

@router.get("/", response_model=list[PengembalianResponse])
def get_all_pengembalian(db: Session = Depends(database.get_db)):
    return pengembalian_service.get_all_pengembalian(db)

@router.get("/{id_pengembalian}", response_model=PengembalianResponse)
def get_pengembalian(id_pengembalian: int, db: Session = Depends(database.get_db)):
    return pengembalian_service.get_pengembalian(id_pengembalian, db)

@router.put("/{id_pengembalian}", response_model=PengembalianResponse)
def update_pengembalian(id_pengembalian: int, request: PengembalianUpdate, db: Session = Depends(database.get_db)):
    return pengembalian_service.update_pengembalian(id_pengembalian, request, db)

@router.delete("/{id_pengembalian}", response_model=MessageResponse)
def delete_pengembalian(id_pengembalian: int, db: Session = Depends(database.get_db)):
    return pengembalian_service.delete_pengembalian(id_pengembalian, db)