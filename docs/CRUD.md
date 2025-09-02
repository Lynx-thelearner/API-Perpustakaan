# API Endpoint Documentation

Dokumentasi endpoint CRUD berdasarkan ERD E-Library

---

## Anggota

| HTTP Method | URL Path              | Kegunaan                              | Request Body | Expected Response | Butuh Auth |
|-------------|-----------------------|---------------------------------------|--------------|------------------|------------|
| GET         | /anggota              | Mendapatkan daftar anggota             | -            | `[{    "nama": "Diaz",    "alamat": "Samarinda",    "no_telp": "088877776666",    "email": "Email@diaz.com",    "id_anggota": 1  }]` | Yes |
| GET         | /anggota/{id_anggota} | Mendapatkan detail anggota tertentu    | -            | Detail anggota (JSON) | Yes |
| POST        | /anggota              | Menambahkan anggota baru               | `{ "nama": "string", "alamat": "string", "no_telp": "string", "email": "string" }` | Data anggota baru | No |
| PUT         | /anggota/{id_anggota} | Update data anggota tertentu           | `{ "nama": "string", "alamat": "string", "no_telp": "string", "email": "string" }` | Data anggota setelah update | Yes |
| DELETE      | /anggota/{id_anggota} | Hapus data anggota tertentu            | -            | Pesan sukses (JSON) | Yes |

---

## Petugas

| HTTP Method | URL Path               | Kegunaan                             | Request Body | Expected Response | Butuh Auth |
|-------------|------------------------|--------------------------------------|--------------|------------------|------------|
| GET         | /petugas               | Mendapatkan daftar petugas            | -            | Daftar petugas (JSON) | Yes |
| GET         | /petugas/{id_petugas}  | Mendapatkan detail petugas tertentu   | -            | Detail petugas (JSON) | Yes |
| POST        | /petugas               | Menambahkan petugas baru              | `{ "nama": "string", "alamat": "string", "no_telp": "string", "email": "string" }` | Data petugas baru | No |
| PUT         | /petugas/{id_petugas}  | Update data petugas tertentu          | `{ "nama": "string", "alamat": "string", "no_telp": "string", "email": "string" }` | Data petugas setelah update | Yes |
| DELETE      | /petugas/{id_petugas}  | Hapus data petugas tertentu           | -            | Pesan sukses (JSON) | Yes |

---

## Kategori

| HTTP Method | URL Path               | Kegunaan                             | Request Body | Expected Response | Butuh Auth |
|-------------|------------------------|--------------------------------------|--------------|------------------|------------|
| GET         | /kategori              | Mendapatkan daftar kategori           | -            | Daftar kategori (JSON) | No |
| GET         | /kategori/{id_kategori}| Mendapatkan detail kategori tertentu  | -            | Detail kategori (JSON) | No |
| POST        | /kategori              | Menambahkan kategori baru             | `{ "nama_kategori": "string" }` | Data kategori baru | Yes |
| PUT         | /kategori/{id_kategori}| Update data kategori tertentu         | `{ "nama_kategori": "string" }` | Data kategori setelah update | Yes |
| DELETE      | /kategori/{id_kategori}| Hapus data kategori tertentu          | -            | Pesan sukses (JSON) | Yes |

---

## Buku

| HTTP Method | URL Path            | Kegunaan                               | Request Body | Expected Response | Butuh Auth |
|-------------|---------------------|----------------------------------------|--------------|------------------|------------|
| GET         | /buku               | Mendapatkan daftar buku                 | -            | Daftar buku (JSON) | No |
| GET         | /buku/{id_buku}     | Mendapatkan detail buku tertentu        | -            | Detail buku (JSON) | No |
| POST        | /buku               | Menambahkan buku baru                   | `{ "judul": "string", "pengarang": "string", "penerbit": "string", "tahun_terbit": 2023, "stok": 10, "id_kategori": 1 }` | Data buku baru | Yes |
| PUT         | /buku/{id_buku}     | Update data buku tertentu               | `{ "judul": "string", "pengarang": "string", "penerbit": "string", "tahun_terbit": 2023, "stok": 15, "id_kategori": 1 }` | Data buku setelah update | Yes |
| DELETE      | /buku/{id_buku}     | Hapus data buku tertentu                | -            | Pesan sukses (JSON) | Yes |

---

## Peminjaman

| HTTP Method | URL Path                   | Kegunaan                               | Request Body | Expected Response | Butuh Auth |
|-------------|----------------------------|----------------------------------------|--------------|------------------|------------|
| GET         | /peminjaman                | Mendapatkan daftar peminjaman           | -            | Daftar peminjaman (JSON) | Yes |
| GET         | /peminjaman/{id_peminjaman}| Mendapatkan detail peminjaman tertentu  | -            | Detail peminjaman (JSON) | Yes |
| POST        | /peminjaman                | Membuat data peminjaman baru            | `{ "id_anggota": 1, "id_petugas": 2, "tanggal_pinjam": "2025-09-01", "tanggal_jatuh_tempo": "2025-09-15", "status": "dipinjam" }` | Data peminjaman baru | Yes |
| PUT         | /peminjaman/{id_peminjaman}| Update data peminjaman tertentu         | `{ "status": "dikembalikan" }` | Data peminjaman setelah update | Yes |
| DELETE      | /peminjaman/{id_peminjaman}| Hapus data peminjaman tertentu          | -            | Pesan sukses (JSON) | Yes |

---

## Detail Peminjaman

| HTTP Method | URL Path                         | Kegunaan                               | Request Body | Expected Response | Butuh Auth |
|-------------|----------------------------------|----------------------------------------|--------------|------------------|------------|
| GET         | /detailpeminjaman                | Mendapatkan daftar detail peminjaman    | -            | Daftar detail peminjaman (JSON) | Yes |
| GET         | /detailpeminjaman/{id_detail}    | Mendapatkan detail data tertentu        | -            | Detail peminjaman (JSON) | Yes |
| POST        | /detailpeminjaman                | Menambahkan detail peminjaman           | `{ "id_peminjaman": 1, "id_buku": 2, "jumlah": 1 }` | Data detail baru | Yes |
| PUT         | /detailpeminjaman/{id_detail}    | Update data detail peminjaman tertentu  | `{ "jumlah": 2 }` | Data detail setelah update | Yes |
| DELETE      | /detailpeminjaman/{id_detail}    | Hapus data detail peminjaman tertentu   | -            | Pesan sukses (JSON) | Yes |

---

## Pengembalian

| HTTP Method | URL Path                        | Kegunaan                               | Request Body | Expected Response | Butuh Auth |
|-------------|---------------------------------|----------------------------------------|--------------|------------------|------------|
| GET         | /pengembalian                   | Mendapatkan daftar pengembalian         | -            | Daftar pengembalian (JSON) | Yes |
| GET         | /pengembalian/{id_pengembalian} | Mendapatkan detail pengembalian tertentu| -            | Detail pengembalian (JSON) | Yes |
| POST        | /pengembalian                   | Membuat data pengembalian baru          | `{ "id_peminjaman": 1, "tanggal_kembali": "2025-09-01", "denda": 5000 }` | Data pengembalian baru | Yes |
| PUT         | /pengembalian/{id_pengembalian} | Update data pengembalian tertentu       | `{ "denda": 10000 }` | Data pengembalian setelah update | Yes |
| DELETE      | /pengembalian/{id_pengembalian} | Hapus data pengembalian tertentu        | -            | Pesan sukses (JSON) | Yes |

---
