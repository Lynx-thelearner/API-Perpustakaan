from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import orm_models, database

from app.models.v1.petugas import petugas


def create_petugas(request: petugas.PetugasCreate, db: Session):
    new_petugas = orm_models.Petugas(
        nama=request.nama,
        alamat=request.alamat,
        no_telp=request.no_telp,
        email=request.email
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
    
    for key, value in request.dict(exclude_unset=True).items():
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
    return {"message": f"Petugas dengan id {id_petugas} berhasil dihapus"}
    