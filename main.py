from fastapi import FastAPI, Depends
import orm_models, database

orm_models.Base.metadata.create_all(bind=database.engine)

from sqlalchemy.orm import Session

from app.models.v1 import (
    UserCreate, UserResponse, UserUpdate,
    BukuCreate, BukuResponse, BukuUpdate,
    KategoriCreate, KategoriResponse, KategoriUpdate,
    PeminjamanCreate, PeminjamanResponse, PeminjamanUpdate,
    PengembalianCreate, PengembalianResponse, PengembalianUpdate,
    MessageResponse,
    Token, TokenPayload
)

from app.api.v1 import routers
from fastapi.middleware.cors import CORSMiddleware

""""Inisialisasi aplikasi"""
app = FastAPI(
    title="E-Library API",
    description="Sistem perpustakaan sederhana dengan FastAPI",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

"""Masukin Router"""
for r in routers:
    app.include_router(r)

""""Awal halaman"""
@app.get("/")
def root():
    return {"message": "Welcome to E-Library API 🚀"}
