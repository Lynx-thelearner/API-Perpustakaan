from app.api.v1.user import user_router
from app.api.v1.buku import buku_router
from app.api.v1.kategori import kategori_router
from app.api.v1.peminjaman import peminjaman_router
from app.api.v1.pengembalian import pengembalian_router
from app.api.v1.auth import auth_router

routers = [
    user_router.router,
    buku_router.router,
    kategori_router.router,
    peminjaman_router.router,
    pengembalian_router.router,
    auth_router.router
]