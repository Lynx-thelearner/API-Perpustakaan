from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import orm_models, database

from app.models.v1.buku import buku
from app.models.v1.msg_response.msg import MessageResponse


def create_buku(request: buku.BukuCreate, db:Session):
    new_buku = orm_models.Buku(
        judul=request.judul,
        pengarang=request.pengarang,
        penerbit=request.penerbit,
        tahun_terbit=request.tahun_terbit,
        stok=request.stok,
        id_kategori=request.id_kategori
    )
    db.add(new_buku)
    db.commit()
    db.refresh(new_buku)
    return new_buku

def get_all_buku(db: Session):
    return db.query(orm_models.Buku).all()

def get_buku(id_buku: int, db: Session):
    buku = db.query(orm_models.Buku).filter(orm_models.Buku.id_buku == id_buku).first()
    if not buku:
        raise HTTPException(status_code=404, detail="Buku not found")
    return buku

def update_buku(id_buku: int, request: buku.BukuUpdate, db: Session):
    buku = db.query(orm_models.Buku).filter(orm_models.Buku.id_buku == id_buku).first()
    if not buku:
        raise HTTPException(status_code=404, detail="Buku not found")
    
    for key, value in request.model_dump(exclude_unset=True).items():
        setattr(buku, key, value)
        
    db.commit()
    db.refresh(buku)
    return buku

def delete_buku(id_buku: int, db: Session):
    buku = db.query(orm_models.Buku).filter(orm_models.Buku.id_buku == id_buku).first()
    if not buku:
        raise HTTPException(status_code=404, detail="Buku not found")
    
    db.delete(buku)
    db.commit()
    return MessageResponse(message=f"Buku dengan id {id_buku} berhasil dihapus")
    