from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
import database, orm_models

from app.models.v1.peminjaman import peminjaman
from app.models.v1.msg_response.msg import MessageResponse

def create_request_peminjaman(request, db, current_user):
  
    #Buat mastikan bukunya ada
    buku = db.query(orm_models.Buku).filter(orm_models.Buku.id_buku == request.id_buku).first()
    if not buku :
        raise HTTPException(status_code=400, detail="Buku tidak ditemukan")
    if buku.stok <= 0:
        raise HTTPException(status_code=400, detail="Stok buku habis")
    
    #Buat nambah data request
    new_request = orm_models.RequestPinjam(
        id_user=current_user.id_user,
        id_buku=request.id_buku,
        jumlah=request.jumlah,
        tgl_request=request.tgl_request,
        status=request.status
    )
    
    db.add(new_request)
    db.commit()
    db.refresh(new_request)
    return new_request

def get_all_requests(db: Session):
    return db.query(orm_models.RequestPinjam).all()

def get_request_peminjaman_by_id(id_request: int, db: Session):
    request_record = db.query(orm_models.RequestPinjam).filter(orm_models.RequestPinjam.id_request == id_request).first()
    if not request_record:
        raise HTTPException(status_code=404, detail="Request not found")
    return request_record

def update_request_peminjaman(id_request: int, request: peminjaman.RequestPeminjamanUpdate, db: Session):
    request_record = db.query(orm_models.RequestPinjam).filter(orm_models.RequestPinjam.id_request == id_request).first()
    if not request_record:
        raise HTTPException(status_code=404, detail="Request not found")
    
    for key, value in request.model_dump(exclude_unset=True).items():
        setattr(request_record, key, value)
        
    db.commit()
    db.refresh(request_record)
    return request_record

def delete_request_peminjaman(id_request: int, db: Session):
    request_record = db.query(orm_models.RequestPinjam).filter(orm_models.RequestPinjam.id_request == id_request).first()
    if not request_record:
        raise HTTPException(status_code=404, detail="Request not found")
    db.delete(request_record)
    db.commit()
    return MessageResponse(message=f"Request dengan id {id_request} berhasil dihapus")

