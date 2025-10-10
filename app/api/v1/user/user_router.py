from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import database
from security.security import require_role, get_current_user
from app.api.v1.user import user_service  
from app.models.v1.user.user import UserCreate, UserResponse, UserUpdate, UserRegister
from app.models.v1.msg_response.msg import MessageResponse 

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

@router.post("/", response_model=UserResponse, dependencies=[Depends(require_role("petugas"))])
def create_user(request: UserCreate, db: Session = Depends(database.get_db)):
    return user_service.create_user(request, db)

@router.get("/", response_model=list[UserResponse], dependencies=[Depends(require_role("petugas"))])
def get_all_user(db: Session = Depends(database.get_db)):
    return user_service.get_all_user(db)

@router.get("/{id_User}", response_model=UserResponse, dependencies=[Depends(require_role("petugas"))])
def get_user(id_User: int, db: Session = Depends(database.get_db)):
    return user_service.get_user(id_User, db)

@router.patch("/{id_User}", response_model=UserResponse, dependencies=[Depends(require_role("petugas"))])
def update_user(id_User: int, request: UserUpdate, db: Session = Depends(database.get_db)):
    return user_service.update_user(id_User, request, db)

@router.delete("/{id_User}", response_model=MessageResponse, dependencies=[Depends(require_role("petugas"))])
def delete_user(id_User: int, db: Session = Depends(database.get_db)):
    return user_service.delete_user(id_User, db)

@router.post("/register", response_model=UserResponse)
def register_user(request: UserRegister, db: Session = Depends(database.get_db)):
    return user_service.register_user(request, db)

@router.get("/{id_user}/profile", response_model=UserResponse)
def get_current_user_profile(current_user=Depends(get_current_user)):
    return UserResponse.model_validate(current_user)