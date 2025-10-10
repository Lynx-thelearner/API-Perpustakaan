from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
import database

from app.api.v1.request_peminjaman import request_peminjaman_service
from app.models.v1.peminjaman.peminjaman import RequestPeminjamanCreate, RequestPeminjamanResponse, RequestPeminjamanUpdate, RequestPeminjaman
from app.models.v1.msg_response.msg import MessageResponse
from security.security import require_role, get_current_user

router = APIRouter(
    prefix="/request-peminjaman",
    tags=["Request Peminjaman"]
)

@router.post("/", response_model=RequestPeminjamanResponse, dependencies=[Depends(require_role("anggota"))])
def create_request_peminjaman(request: RequestPeminjamanCreate, db: Session = Depends(database.get_db), current_user=Depends(get_current_user)):
    return request_peminjaman_service.create_request_peminjaman(request, db, current_user)

@router.get("/", response_model=list[RequestPeminjamanResponse], dependencies=[Depends(require_role("petugas"))])
def get_all_request(db: Session = Depends(database.get_db)):
    return request_peminjaman_service.get_all_requests(db)

@router.get("/{id_request}", response_model=RequestPeminjamanResponse, dependencies=[Depends(require_role("petugas"))])
def get_request_by_id(id_request: int, db: Session = Depends(database.get_db)):
    return request_peminjaman_service.get_request_peminjaman_by_id(id_request, db)

@router.patch("/{id_request}", response_model=RequestPeminjamanResponse, dependencies=[Depends(require_role("petugas"))])
def update_request(id_request: int, request: RequestPeminjamanUpdate, db: Session = Depends(database.get_db)):
    return request_peminjaman_service.update_request_peminjaman(id_request, request, db)

@router.delete("/{id_request}", response_model=MessageResponse, dependencies=[Depends(require_role("petugas"))])
def delete_request(id_request: int, db: Session = Depends(database.get_db)):
    return request_peminjaman_service.delete_request_peminjaman(id_request, db)

