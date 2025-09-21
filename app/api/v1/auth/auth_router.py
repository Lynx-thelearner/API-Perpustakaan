from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from app.api.v1.auth.auth_service import login_anggota, login_petugas
from app.models.v1.token.token_schema import Token

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login_petugas", response_model=Token)
def login_petugas_endpoint(nama: str, password: str, db: Session = Depends(get_db)):
    return login_petugas(db, nama, password)

@router.post("/login_anggota", response_model=Token)
def login_anggota_endpoint(nama: str, password: str, db: Session = Depends(get_db)):
    return login_anggota(db, nama, password)
