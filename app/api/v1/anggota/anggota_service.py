from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import orm_models, database
from app.models.v1.anggota import anggota
from app.models.v1.msg_response.msg import MessageResponse
from security import hash_password, verify_password

def create_anggota(request: anggota.AnggotaCreate, db: Session):
    new_anggota = orm_models.Anggota(
        nama=request.nama,
        alamat=request.alamat,
        no_telp=request.no_telp,
        email=request.email,
        password=hash_password(request.password)
    )
    db.add(new_anggota)
    db.commit()
    db.refresh(new_anggota)
    return new_anggota

def get_all_anggota(db: Session):
    return db.query(orm_models.Anggota).all()

def get_anggota(id_anggota: int, db: Session):
    anggota = db.query(orm_models.Anggota).filter(orm_models.Anggota.id_anggota == id_anggota).first()
    if not anggota:
        raise HTTPException(status_code=404, detail="Anggota not found")
    return anggota

def update_anggota(id_anggota: int, request: anggota.AnggotaUpdate, db: Session):
    anggota = db.query(orm_models.Anggota).filter(orm_models.Anggota.id_anggota == id_anggota).first()
    if not anggota:
        raise HTTPException(status_code=404, detail="Anggota not found")
    
    data = request.dict(exclude_unset=True)
    if "password" in data and data["password"] is not None:
        data["password"] = hash_password(data["password"])
    
    for key, value in data.items():
        setattr(anggota, key, value)
        
    db.commit()
    db.refresh(anggota)
    return anggota

def delete_anggota(id_anggota: int, db: Session):
    anggota = db.query(orm_models.Anggota).filter(orm_models.Anggota.id_anggota == id_anggota).first()
    if not anggota:
        raise HTTPException(status_code=404, detail="Anggota not found")
    
    db.delete(anggota)
    db.commit()
    return MessageResponse(message="Anggota dengan id {id_anggota} berhasil dihapus")
