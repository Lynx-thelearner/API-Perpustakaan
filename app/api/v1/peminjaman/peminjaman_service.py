from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
import database

from app.models.v1.peminjaman import peminjaman
from app.models.v1.msg_response.msg import MessageResponse


def create_peminjaman(request: peminjaman.PeminjamanCreate, db: Session):
    new_peminjaman = peminjaman.PeminjamanModel(
    id_anggota=request.id_anggota,
    id_buku=request.id_buku,
    id_petugas=request.id_petugas,
    jumlah=request.jumlah,
    tgl_pinjam=request.tgl_pinjam,
    tgl_kembali=request.tgl_kembali,
    status=request.status
)
    db.add(new_peminjaman)
    db.commit()
    db.refresh(new_peminjaman)
    return new_peminjaman

def get_all_peminjaman(db: Session):
    return db.query(peminjaman.PeminjamanModel).all()

def get_peminjaman(id_peminjaman: int, db: Session):
    peminjaman_record = db.query(peminjaman.PeminjamanModel).filter(peminjaman.PeminjamanModel.id_peminjaman == id_peminjaman).first()
    if not peminjaman_record:
        raise HTTPException(status_code=404, detail="Peminjaman not found")
    return peminjaman_record

def update_peminjaman(id_peminjaman: int, request: peminjaman.PeminjamanUpdate, db: Session):
    peminjaman = db.query(peminjaman.PeminjamanModel).filter(peminjaman.PeminjamanModel.id_peminjaman == id_peminjaman).first()
    if not peminjaman:
        raise HTTPException(status_code=404, detail="Peminjaman not found")
    for key, value in request.dict(exclude_unset=True).items():
        setattr(peminjaman, key, value)
        
    db.commit()
    db.refresh(peminjaman)
    return peminjaman

def delete_peminjaman(id_peminjaman: int, db: Session):
    peminjaman = db.query(peminjaman.PeminjamanModel).filter(peminjaman.PeminjamanModel.id_peminjaman == id_peminjaman).first()
    if not peminjaman:
        raise HTTPException(status_code=404, detail="Peminjaman not found")
    
    db.delete(peminjaman)
    db.commit()
    return MessageResponse(message=f"Peminjaman dengan id {id_peminjaman} berhasil dihapus")
