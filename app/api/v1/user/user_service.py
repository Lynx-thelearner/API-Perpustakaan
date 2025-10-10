from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import orm_models, database
from app.models.v1.user import user
from app.models.v1.msg_response.msg import MessageResponse
from security.security import hash_password, verify_password


def create_user(request: user.UserCreate, db: Session):
    new_user = orm_models.User(
        nama=request.nama,
        username=request.username,
        alamat=request.alamat,
        no_telp=request.no_telp,
        email=request.email,
        password=hash_password(request.password),
        role=request.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_user(db: Session):
    return db.query(orm_models.User).all()

def get_user(id_user: int, db: Session):
    user = db.query(orm_models.User).filter(orm_models.User.id_user == id_user).first()
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    return user

def update_user(id_user: int, request: user.UserUpdate, db: Session):
    user = db.query(orm_models.User).filter(orm_models.User.id_user == id_user).first()
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    
    data = request.model_dump(exclude_unset=True)
    if "password" in data and data["password"] is not None:
        data["password"] = hash_password(data["password"])
    
    for key, value in data.items():
        setattr(user, key, value)
        
    db.commit()
    db.refresh(user)
    return user

def delete_user(id_user: int, db: Session):
    user = db.query(orm_models.User).filter(orm_models.User.id_user == id_user).first()
    if not user:
        raise HTTPException(status_code=404, detail="user not found")
    
    peminjaman_aktif = db.query(orm_models.Peminjaman).filter(
        orm_models.Peminjaman.id_user == id_user, orm_models.Peminjaman.status == orm_models.StatusEnum.dipinjam
    ).first()
    if peminjaman_aktif:
        raise HTTPException(status_code=400, detail="user memiliki peminjaman aktif dan tidak dapat dihapus")
    
    db.delete(user)
    db.commit()
    return MessageResponse(message=f"user dengan id {id_user} berhasil dihapus")

def register_user(Request: user.UserRegister, db: Session):
    new_user = orm_models.User(
        nama=Request.nama,
        username=Request.username,
        alamat=Request.alamat,
        no_telp=Request.no_telp,
        email=Request.email,
        password=hash_password(Request.password),
        role="anggota" #Fixed role jadi anggota
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
