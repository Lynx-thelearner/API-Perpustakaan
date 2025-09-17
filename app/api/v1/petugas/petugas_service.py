from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import orm_models, database

from app.models.v1.petugas import petugas
from app.models.v1.msg_response.msg import MessageResponse
from security import hash_password, verify_password



def create_petugas(request: petugas.PetugasCreate, db: Session):
    new_petugas = orm_models.Petugas(
        nama=request.nama,
        alamat=request.alamat,
        no_telp=request.no_telp,
        email=request.email,
        password=hash_password(request.password)
    )
    db.add(new_petugas)
    db.commit()
    db.refresh(new_petugas)
    return new_petugas

def get_all_petugas(db: Session):
    return db.query(orm_models.Petugas).all()

def get_petugas(id_petugas: int,db: Session):
    petugas = db.query(orm_models.Petugas).filter(orm_models.Petugas.id_petugas == id_petugas).first()
    if not petugas:
        raise HTTPException(status_code=404, detail="Petugas not found")
    return petugas

def update_petugas(id_petugas: int, request: petugas.PetugasUpdate, db: Session):
    petugas = db.query(orm_models.Petugas).filter(orm_models.Petugas.id_petugas == id_petugas).first()
    if not petugas:
        raise HTTPException(status_code=404, detail="Petugas not found")
    
    data = request.dict(exclude_unset=True)
    if "password" in data and data["password"] is not None:
        data["password"] = hash_password(data["password"])
    
    for key, value in data.items():
        setattr(petugas, key, value)
        
    db.commit()
    db.refresh(petugas)
    return petugas

def delete_petugas(id_petugas: int, db: Session):
    petugas = db.query(orm_models.Petugas).filter(orm_models.Petugas.id_petugas == id_petugas).first()
    if not petugas:
        raise HTTPException(status_code=404, detail="Petugas not found")
    
    db.delete(petugas)
    db.commit()
    return MessageResponse(message=f"Petugas {petugas.nama} berhasil dihapus")
    