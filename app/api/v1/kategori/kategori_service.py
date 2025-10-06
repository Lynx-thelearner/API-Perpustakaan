from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import orm_models, database

from app.models.v1.kategori import kategori
from app.models.v1.msg_response.msg import MessageResponse


def create_kategori (request: kategori.KategoriCreate, db:Session):
    new_kategori = orm_models.Kategori(
        nama_kategori=request.nama_kategori
    )
    db.add(new_kategori)
    db.commit()
    db.refresh(new_kategori)
    return new_kategori

def get_all_kategori(db: Session):
    return db.query(orm_models.Kategori).all()

def get_kategori(id_kategori: int, db: Session):
    kategori = db.query(orm_models.Kategori).filter(orm_models.Kategori.id_kategori == id_kategori).first()
    if not kategori:
        raise HTTPException(status_code=404, detail="Kategori not found")
    return kategori

def update_kategori(id_kategori: int, request: kategori.KategoriUpdate, db: Session):
    kategori = db.query(orm_models.Kategori).filter(orm_models.Kategori.id_kategori == id_kategori).first()
    if not kategori:
        raise HTTPException(status_code=404, detail="Kategori not found")
    
    for key, value in request.model_dump(exclude_unset=True).items():
        setattr(kategori, key, value)
        
    db.commit()
    db.refresh(kategori)
    return kategori

def delete_kategori(id_kategori: int, db: Session):
    kategori = db.query(orm_models.Kategori).filter(orm_models.Kategori.id_kategori == id_kategori).first()
    if not kategori:
        raise HTTPException(status_code=404, detail="Kategori not found")
    
    db.delete(kategori)
    db.commit()
    return MessageResponse(message=f"Kategori {kategori.nama_kategori} berhasil dihapus")