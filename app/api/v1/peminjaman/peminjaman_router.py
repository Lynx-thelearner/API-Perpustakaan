from fastapi import HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
import database

from app.api.v1.peminjaman import peminjaman_service
from app.models.v1.peminjaman.peminjaman import PeminjamanCreate, PeminjamanResponse, PeminjamanUpdate
from app.models.v1.msg_response.msg import MessageResponse
from security.security import require_role, get_current_user

router = APIRouter(
    prefix="/peminjaman",
    tags=["Peminjaman"]
)

@router.post("/", response_model=PeminjamanResponse)
def create_peminjaman(request: PeminjamanCreate, db: Session = Depends(database.get_db)):
    return peminjaman_service.create_peminjaman(request, db)

@router.get("/", response_model=list[PeminjamanResponse], dependencies=[Depends(require_role("petugas"))])
def get_all_peminjaman(db: Session = Depends(database.get_db)):
    return peminjaman_service.get_all_peminjaman(db)

@router.get("/{id_peminjaman}", response_model=PeminjamanResponse, dependencies=[Depends(require_role("petugas"))])
def get_peminjaman(id_peminjaman: int, db: Session = Depends(database.get_db)):
    return peminjaman_service.get_peminjaman(id_peminjaman, db)

@router.patch("/{id_peminjaman}", response_model=PeminjamanResponse, dependencies=[Depends(require_role("petugas"))])
def update_peminjaman(id_peminjaman: int, request: PeminjamanUpdate, db: Session = Depends(database.get_db)):
    return peminjaman_service.update_peminjaman(id_peminjaman, request, db)

@router.delete("/{id_peminjaman}", response_model=MessageResponse, dependencies=[Depends(require_role("petugas"))])
def delete_peminjaman(id_peminjaman: int, db: Session = Depends(database.get_db)):
    return peminjaman_service.delete_peminjaman(id_peminjaman, db)