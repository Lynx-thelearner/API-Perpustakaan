from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from orm_models import Anggota, Petugas
from app.models.v1.token.token_schema import Token
from security import verify_password, create_access_token

def aunthenticate_petugas(db: Session, nama: str, password: str) -> Petugas:
    """Authenticate petugas by nama and password."""
    petugas = db.query(Petugas).filter(Petugas.nama == nama).first()
    if not petugas or not verify_password(password, petugas.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return petugas

def login_petugas(db: Session, nama: str, password: str) -> Token:
    """Login petugas and return access token."""
    petugas = aunthenticate_petugas(db, nama, password)
    access_token = create_access_token(subject=str(petugas.id_petugas), extra={"role": "petugas"})
    return Token(access_token=access_token, token_type="bearer")

def aunthenticate_anggota(db: Session, nama: str, password: str) -> Anggota:
    """Authenticate anggota by nama and password."""
    anggota = db.query(Anggota).filter(Anggota.nama == nama).first()
    if not anggota or not verify_password(password, anggota.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return anggota

def login_anggota(db: Session, nama: str, password: str) -> Token:
    """Login anggota and return access token."""
    anggota = aunthenticate_anggota(db, nama, password)
    access_token = create_access_token(subject=str(anggota.id_anggota), extra={"role": "anggota"})
    return Token(access_token=access_token, token_type="bearer")


