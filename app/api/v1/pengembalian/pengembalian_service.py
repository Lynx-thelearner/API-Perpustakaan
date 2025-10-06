from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import orm_models

from app.models.v1.pengembalian import pengembalian
from app.models.v1.msg_response.msg import MessageResponse

def create_pengembalian(request: pengembalian.PengembalianCreate, db: Session):
    #Buat ngecek data peminjaman
    peminjaman = db.query(orm_models.Peminjaman).filter(orm_models.Peminjaman.id_peminjaman == request.id_peminjaman).first()
    
    if not peminjaman :
        raise HTTPException(status_code=404, detail="Data peminjaman tidak ditemukan")
    
    #Validasi status
    if peminjaman.status == orm_models.StatusEnum.dikembalikan or peminjaman.status == orm_models.StatusEnum.hilang:
        raise HTTPException(status_code=400, detail="Buku sudah dikembalikan atau hilang")
    
    #Ubah status peminjaman jadi kembali
    peminjaman.status = orm_models.StatusEnum.dikembalikan
    peminjaman.tgl_kembali = request.tgl_kembali
    
    # Buku berhasil dikembalikan → stok bertambah
    buku = db.query(orm_models.Buku).filter(orm_models.Buku.id_buku == peminjaman.id_buku).first()
    if buku:
        buku.stok += peminjaman.jumlah
            
    #Ini buat nambah data pengembalian baru
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
    
    for key, value in request.model_dump(exclude_unset=True).items():
        setattr(pengembalian, key, value)
        
    db.commit()
    db.refresh(pengembalian)
    return pengembalian

def delete_pengembalian(id_pengembalian: int, db: Session):
    pengembalian = db.query(orm_models.Pengembalian).filter(orm_models.Pengembalian.id_pengembalian == id_pengembalian).first()
    if not pengembalian:
        raise HTTPException(status_code=404, detail="Pengembalian not found")
    
   # Mengembalikan status peminjaman agar dianggap belum dikembalikan
    peminjaman = db.query(orm_models.Peminjaman).filter(orm_models.Peminjaman.id_peminjaman == pengembalian.id_peminjaman).first()
    if peminjaman:
        peminjaman.status = orm_models.StatusEnum.dipinjam
        peminjaman.tgl_kembali = None  # Reset tgl_kembali karena buku belum dikembalikan
        
        #Update stok buku
        buku = db.query(orm_models.Buku).filter(orm_models.Buku.id_buku == peminjaman.id_buku).first()
        if buku and buku.stok >= peminjaman.jumlah:
            buku.stok -= peminjaman.jumlah
    
    db.delete(pengembalian)
    db.commit()
    return MessageResponse(message=f"Pengembalian dengan id {id_pengembalian} telah dihapus")

