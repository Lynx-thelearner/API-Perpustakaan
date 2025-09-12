from .anggota import anggota_router
from .buku import buku_router
from .kategori import kategori_router
from .peminjaman import peminjaman_router
from .pengembalian import pengembalian_router
from .petugas import petugas_router

routers = [
    anggota_router.router,
    buku_router.router,
    kategori_router.router,
    peminjaman_router.router,
    pengembalian_router.router,
    petugas_router.router,
]
