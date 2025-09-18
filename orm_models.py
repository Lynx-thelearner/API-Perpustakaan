from sqlalchemy import Column, Integer, String, DATE, ForeignKey
from database import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Enum
import enum

class Anggota(Base):
    __tablename__ = "anggota"

    id_anggota = Column(Integer, primary_key=True, index=True)
    nama = Column(String, nullable=False, index=True)
    alamat = Column(String, nullable=False)
    no_telp = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    
    peminjaman = relationship("Peminjaman", back_populates="anggota")

class Petugas(Base):
    __tablename__ = "petugas"

    id_petugas = Column(Integer, primary_key=True, index=True)
    nama = Column(String, nullable=False, index=True)
    alamat = Column(String, nullable=False)
    no_telp = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)
    
    peminjaman = relationship("Peminjaman", back_populates="petugas")
    
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
    
    kategori = relationship("Kategori", back_populates="buku")
    peminjaman = relationship("Peminjaman", back_populates="buku")
    
class Kategori(Base):
    __tablename__ = "kategori"

    id_kategori = Column(Integer, primary_key=True, index=True)
    nama_kategori = Column(String, nullable=False, index=True)
    
    buku = relationship("Buku", back_populates="kategori")
    
class StatusEnum(enum.Enum):
    dipinjam = "dipinjam"
    dikembalikan = "dikembalikan"
    hilang = "hilang"
    
class Peminjaman(Base):
    __tablename__ = "peminjaman"

    id_peminjaman = Column(Integer, primary_key=True, index=True)
    id_anggota = Column(Integer, ForeignKey("anggota.id_anggota"), nullable=False)
    id_petugas = Column(Integer, ForeignKey("petugas.id_petugas"), nullable=False)
    id_buku = Column(Integer, ForeignKey("buku.id_buku"), nullable=False, index=True)
    jumlah = Column(Integer, nullable=False)
    tgl_pinjam = Column(DATE, nullable=False)
    tgl_kembali = Column(DATE, nullable=True)
    status = Column(Enum(StatusEnum), nullable=False, default=StatusEnum.dipinjam)
    
    anggota = relationship("Anggota", back_populates="peminjaman")
    petugas = relationship("Petugas", back_populates="peminjaman")
    pengembalian = relationship("Pengembalian", back_populates="peminjaman", uselist=False)
    buku = relationship("Buku", back_populates="peminjaman")
    
class Pengembalian(Base):
    __tablename__ = "pengembalian"

    id_pengembalian = Column(Integer, primary_key=True, index=True)
    id_peminjaman = Column(Integer, ForeignKey("peminjaman.id_peminjaman"), nullable=False, index=True)
    tgl_kembali = Column(DATE, nullable=False, index=True)
    denda = Column(Integer, nullable=False)
    
    peminjaman = relationship("Peminjaman", back_populates="pengembalian")