from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
import database, orm_models

from app.models.v1.peminjaman import peminjaman
from app.models.v1.msg_response.msg import MessageResponse


def create_peminjaman(request: peminjaman.PeminjamanCreate, db: Session):
    
    #Buat mastikan id_user itu rolenya anggota
    user = db.query(orm_models.User).filter(orm_models.User.id_user == request.id_user).first()
    if not user or user.role != orm_models.RoleEnum.anggota:
        raise HTTPException(status_code=400, detail="User bukan anggota")
    
    #Buat mastikan id_petugas itu rolenya petugas
    petugas = db.query(orm_models.User).filter(orm_models.User.id_user == request.id_petugas).first()
    if not petugas or petugas.role != orm_models.RoleEnum.petugas:
        raise HTTPException(status_code=400, detail="User bukan petugas")
    
    #Buat mastikan bukunya ada terus ada stoknya
    buku = db.query(orm_models.Buku).filter(orm_models.Buku.id_buku == request.id_buku).first()
    if not buku :
        raise HTTPException(status_code=400, detail="Buku tidak ditemukan")
    if buku.stok < 0:
        raise HTTPException(status_code=400, detail="Stok buku habis")
    
    #Ini buat nambah data peminjaman baru
    new_peminjaman = orm_models.Peminjaman(
        id_user=request.id_user,
        id_buku=request.id_buku,
        id_petugas=request.id_petugas,
        jumlah=request.jumlah,
        tgl_pinjam=request.tgl_pinjam,
        tgl_kembali=request.tgl_kembali,
        status=request.status
)
    
    buku.stok -= request.jumlah  # Kurangi stok buku saat ada peminjaman baru
    
    db.add(new_peminjaman)
    db.commit()
    db.refresh(new_peminjaman)
    return new_peminjaman

def get_all_peminjaman(db: Session):
    return db.query(orm_models.Peminjaman).all()

def get_peminjaman(id_peminjaman: int, db: Session):
    peminjaman_record = db.query(orm_models.Peminjaman).filter(orm_models.Peminjaman.id_peminjaman == id_peminjaman).first()
    if not peminjaman_record:
        raise HTTPException(status_code=404, detail="Peminjaman not found")
    return peminjaman_record

def update_peminjaman(id_peminjaman: int, request: peminjaman.PeminjamanUpdate, db: Session):
    peminjaman = db.query(orm_models.Peminjaman).filter(orm_models.Peminjaman.id_peminjaman == id_peminjaman).first()
    if not peminjaman:
        raise HTTPException(status_code=404, detail="Peminjaman not found")
    for key, value in request.model_dump(exclude_unset=True).items():
        setattr(peminjaman, key, value)
        
    db.commit()
    db.refresh(peminjaman)
    return peminjaman

def delete_peminjaman(id_peminjaman: int, db: Session):
    peminjaman = db.query(orm_models.Peminjaman).filter(orm_models.Peminjaman.id_peminjaman == id_peminjaman).first()
    if not peminjaman:
        raise HTTPException(status_code=404, detail="Peminjaman not found")
    
    db.delete(peminjaman)
    db.commit()
    return MessageResponse(message=f"Peminjaman dengan id {id_peminjaman} berhasil dihapus")
