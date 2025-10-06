from .user import user_router
from .buku import buku_router
from .kategori import kategori_router
from .peminjaman import peminjaman_router
from .pengembalian import pengembalian_router
from .auth import auth_router

routers = [
    user_router.router,
    buku_router.router,
    kategori_router.router,
    peminjaman_router.router,
    pengembalian_router.router,
    auth_router.router
]
