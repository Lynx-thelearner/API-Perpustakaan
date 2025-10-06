from sqlalchemy import Column, Integer, String, DATE, ForeignKey, DECIMAL
from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Enum
import enum

# --- Enum untuk Role User ---
class RoleEnum(enum.Enum):
    anggota = "anggota"
    petugas = "petugas"

class User(Base):
    __tablename__ = "user"

    id_user = Column(Integer, primary_key=True, index=True)
    nama = Column(String, nullable=False, index=True)
    username = Column(String, nullable=False, unique=True, index=True)
    alamat = Column(String, nullable=False)
    no_telp = Column(String, nullable=False)
    email = Column(String, nullable=False ,index=True)
    password = Column(String, nullable=False)
    role = Column(Enum(RoleEnum), nullable=False, default=RoleEnum.anggota)
    
     # relasi: user bisa meminjam buku
    peminjaman = relationship("Peminjaman", back_populates="user", foreign_keys="Peminjaman.id_user")
    # relasi: user bisa melayani peminjaman (Untuk Petugas)
    peminjaman_dilayani = relationship("Peminjaman", back_populates="petugas", foreign_keys="Peminjaman.id_petugas")
    
class Buku(Base):
    __tablename__ = "buku"

    id_buku = Column(Integer, primary_key=True, index=True)
    judul = Column(String, nullable=False, index=True)
    pengarang = Column(String, nullable=False)
    penerbit = Column(String, nullable=False)
    tahun_terbit = Column(Integer, nullable=False)
    stok = Column(Integer, nullable=False)
    cover = Column(String, nullable=True)
    id_kategori = Column(Integer, ForeignKey("kategori.id_kategori"), nullable=False)
    
    # relasi: buku memiliki satu kategori
    kategori = relationship("Kategori", back_populates="buku")
    # relasi: buku ke peminjaman
    peminjaman = relationship("Peminjaman", back_populates="buku")
    
class Kategori(Base):
    __tablename__ = "kategori"

    id_kategori = Column(Integer, primary_key=True, index=True)
    nama_kategori = Column(String, nullable=False, index=True)
    
    # relasi: kategori memiliki banyak buku
    buku = relationship("Buku", back_populates="kategori")
    
    # Enum untuk status peminjaman
class StatusEnum(enum.Enum):
    dipinjam = "dipinjam"
    dikembalikan = "dikembalikan"
    hilang = "hilang"
    
class Peminjaman(Base):
    __tablename__ = "peminjaman"

    id_peminjaman = Column(Integer, primary_key=True, index=True)
    id_user = Column(Integer, ForeignKey("user.id_user"), nullable=False)      # siapa yang pinjam
    id_petugas = Column(Integer, ForeignKey("user.id_user"), nullable=False)   # siapa yang melayani
    id_buku = Column(Integer, ForeignKey("buku.id_buku"), nullable=False)
    jumlah = Column(Integer, nullable=False)
    tgl_pinjam = Column(DATE, nullable=False)
    tgl_kembali = Column(DATE, nullable=True)
    status = Column(Enum(StatusEnum), nullable=False, default=StatusEnum.dipinjam)

    # Relasi user yang minjam
    user = relationship("User", back_populates="peminjaman", foreign_keys=[id_user])
    # Relasi user yang melayani (petugas)
    petugas = relationship("User", back_populates="peminjaman_dilayani", foreign_keys=[id_petugas])
    buku = relationship("Buku", back_populates="peminjaman")
    # Relasi ke pengembalian (satu ke satu)
    pengembalian = relationship("Pengembalian", back_populates="peminjaman", uselist=False)


class Pengembalian(Base):
    __tablename__ = "pengembalian"

    id_pengembalian = Column(Integer, primary_key=True, index=True)
    id_peminjaman = Column(Integer, ForeignKey("peminjaman.id_peminjaman"), nullable=False, index=True)
    tgl_kembali = Column(DATE, nullable=False, index=True)
    denda = Column(DECIMAL, nullable=False)
    
    # Relasi ke peminjaman
    peminjaman = relationship("Peminjaman", back_populates="pengembalian")