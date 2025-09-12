from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import orm_models

from app.models.v1.pengembalian import pengembalian

def create_pengembalian(request: pengembalian.PengembalianCreate, db: Session):
    new_pengembalian = orm_models.Pengembalian(
        id_peminjaman=request.id_peminjaman,
        tgl_kembali=request.tgl_kembali,
        denda=request.denda
    )
    db.add(new_pengembalian)
    db.commit()
    db.refresh(new_pengembalian)
    return new_pengembalian

def get_all_pengembalian(db: Session):
    return db.query(orm_models.Pengembalian).all()

def get_pengembalian(id_pengembalian: int, db: Session):
    pengembalian = db.query(orm_models.Pengembalian).filter(orm_models.Pengembalian.id_pengembalian == id_pengembalian).first()
    if not pengembalian:
        raise HTTPException(status_code=404, detail="Pengembalian not found")
    return pengembalian

def update_pengembalian(id_pengembalian: int, request: pengembalian.PengembalianUpdate, db: Session):
    pengembalian = db.query(orm_models.Pengembalian).filter(orm_models.Pengembalian.id_pengembalian == id_pengembalian).first()
    if not pengembalian:
        raise HTTPException(status_code=404, detail="Pengembalian not found")
    
    for key, value in request.dict(exclude_unset=True).items():
        setattr(pengembalian, key, value)
        
    db.commit()
    db.refresh(pengembalian)
    return pengembalian

def delete_pengembalian(id_pengembalian: int, db: Session):
    pengembalian = db.query(orm_models.Pengembalian).filter(orm_models.Pengembalian.id_pengembalian == id_pengembalian).first()
    if not pengembalian:
        raise HTTPException(status_code=404, detail="Pengembalian not found")
    
    db.delete(pengembalian)
    db.commit()
    return {"message": f"Pengembalian dengan id {id_pengembalian} berhasil dihapus"}

