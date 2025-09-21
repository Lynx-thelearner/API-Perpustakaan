from fastapi import FastAPI, Depends
import orm_models, database

orm_models.Base.metadata.create_all(bind=database.engine)

from sqlalchemy.orm import Session

from app.models.v1 import (
    AnggotaCreate, AnggotaResponse, AnggotaUpdate,
    BukuCreate, BukuResponse, BukuUpdate,
    KategoriCreate, KategoriResponse, KategoriUpdate,
    PeminjamanCreate, PeminjamanResponse, PeminjamanUpdate,
    PengembalianCreate, PengembalianResponse, PengembalianUpdate,
    PetugasCreate, PetugasResponse, PetugasUpdate,
    MessageResponse,
    Token, TokenPayload
)

from app.api.v1 import routers

""""Inisialisasi aplikasi"""
app = FastAPI(
    title="E-Library API",
    description="Sistem perpustakaan sederhana dengan FastAPI",
    version="1.0.0"
)

"""Masukin Router"""
for r in routers:
    app.include_router(r)

""""Awal halaman"""
@app.get("/")
def root():
    return {"message": "Welcome to E-Library API 🚀"}
