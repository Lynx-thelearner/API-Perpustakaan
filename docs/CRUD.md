# API Endpoint Documentation

Dokumentasi endpoint CRUD berdasarkan ERD E-Library

---

## Anggota

| HTTP Method | URL Path              | Kegunaan                              | Request Body | Expected Response | Butuh Auth |
|-------------|-----------------------|---------------------------------------|--------------|------------------|------------|
| GET         | /anggota              | Mendapatkan daftar anggota             | -            | `[{    "nama": "Diaz",    "alamat": "Samarinda",    "no_telp": "088877776666",    "email": "Email@diaz.com",    "id_anggota": 1  }]` | Petugas only |
| GET         | /anggota/{id_anggota} | Mendapatka data anggota tertentu    | -            | `[{    "nama": "Diaz",    "alamat": "Samarinda",    "no_telp": "088877776666",    "email": "Email@diaz.com",    "id_anggota": 1  }]` | self dan petugas |
| POST        | /anggota              | Menambahkan anggota baru               | `{ "nama": "string", "alamat": "string", "no_telp": "string", "email": "string" }` | Data anggota baru | No |
| PUT         | /anggota/{id_anggota} | Update data anggota tertentu           | `{"no_telp": "000011112222"}` | `[{    "nama": "Diaz",    "alamat": "Samarinda",    "no_telp": "000011112222",    "email": "Email@diaz.com",    "id_anggota": 1  }]` | self dan petugas |
| DELETE      | /anggota/{id_anggota} | Hapus data anggota tertentu            | -            | `{"message": "Anggota dengan id 2 berhasil dihapus"}` | Petugas only |

---

## Petugas

| HTTP Method | URL Path               | Kegunaan                             | Request Body | Expected Response | Butuh Auth |
|-------------|------------------------|--------------------------------------|--------------|------------------|------------|
| GET         | /petugas               | Mendapatkan daftar petugas            | -            | `[{    "nama": "Petugas-Diaz",    "alamat": "Samarinda",    "no_telp": "088877776666",    "email": "Email@diaz.com",    "id_anggota": 1  }]` | Petugas only |
| GET         | /petugas/{id_petugas}  | Mendapatka data petugas tertentu   | -            | `[{    "nama": "Petugas-Diaz",    "alamat": "Samarinda",    "no_telp": "088877776666",    "email": "Email@diaz.com",    "id_anggota": 1  }]` | Petugas only |
| POST        | /petugas               | Menambahkan petugas baru              | `{ "nama": "string", "alamat": "string", "no_telp": "string", "email": "string" }` | Data petugas baru | No |
| PUT         | /petugas/{id_petugas}  | Update data petugas tertentu          | `{ "nama": "Lynx" }` | `[{    "nama": "Lynx",    "alamat": "Samarinda",    "no_telp": "088877776666",    "email": "Email@diaz.com",    "id_anggota": 1  }]` | Petugas only |
| DELETE      | /petugas/{id_petugas}  | Hapus data petugas tertentu           | -            | `{"message": "Petugas dengan id 2 berhasil dihapus"}` | Petugas only |

---

## Kategori

| HTTP Method | URL Path               | Kegunaan                             | Request Body | Expected Response | Butuh Auth |
|-------------|------------------------|--------------------------------------|--------------|------------------|------------|
| GET         | /kategori              | Mendapatkan daftar kategori           | -            | `[{"nama":"Fantasi", "id_kategori": 1 }]` | No |
| GET         | /kategori/{id_kategori}| Mendapatkan kategori tertentu  | -            | `[{"nama":"Fantasi", "id_kategori": 1}]` | No |
| POST        | /kategori              | Menambahkan kategori baru             | `{ "nama_kategori": "string" }` | Data kategori baru | Petugas only |
| PUT         | /kategori/{id_kategori}| Update data kategori tertentu         | `{ "nama_kategori": "Romance" }` | `[{"nama":"Romance", "id_kategori": 1}]` | Petugas only |
| DELETE      | /kategori/{id_kategori}| Hapus data kategori tertentu          | -            | Pesan sukses (JSON) | Petugas only |

---

## Buku

| HTTP Method | URL Path            | Kegunaan                               | Request Body | Expected Response | Butuh Auth |
|-------------|---------------------|----------------------------------------|--------------|------------------|------------|
| GET         | /buku               | Mendapatkan daftar buku                 | -            | `{  "judul": "Laskar Pelangi",  "pengarang": "Andrea Hirata",  "penerbit": "Bentang Pustaka",  "tahun_terbit": 2005,  "stok": 10,  "id_kategori": 1}` | No |
| GET         | /buku/{id_buku}     | Mendapatka data buku tertentu        | -            | `{  "judul": "Laskar Pelangi",  "pengarang": "Andrea Hirata",  "penerbit": "Bentang Pustaka",  "tahun_terbit": 2005,  "stok": 10,  "id_kategori": 1}` | No |
| POST        | /buku               | Menambahkan buku baru                   | `{ "judul": "string", "pengarang": "string", "penerbit": "string", "tahun_terbit": 2023, "stok": 10, "id_kategori": 1 }` | Data buku baru | Petugas only |
| PUT         | /buku/{id_buku}     | Update data buku tertentu               | `{ "stok": 15}` | `{  "judul": "Laskar Pelangi(Revisi)",  "pengarang": "Andrea Hirata",  "penerbit": "Bentang Pustaka",  "tahun_terbit": 2005,  "stok": 15,  "id_kategori": 1}` | Petugas only |
| DELETE      | /buku/{id_buku}     | Hapus data buku tertentu                | -            | `{"message": Buku dengan id 1 berhasil dihapus"}` | Petugas only |

---

## Peminjaman

| HTTP Method | URL Path                   | Kegunaan                               | Request Body | Expected Response | Butuh Auth |
|-------------|----------------------------|----------------------------------------|--------------|------------------|------------|
| GET         | /peminjaman                | Mendapatkan daftar peminjaman           | -            | `{"id_peminjaman": 12,  "id_anggota": 5,  "id_petugas": 2, "id_buku":1, "jml_buku":3,  "tgl_pinjam": "2025-09-02",  "tgl_kembali": null,  "status": "dipinjam"}` | Anggota dan petugas |
| GET         | /peminjaman/{id_peminjaman}| Mendapatka data peminjaman tertentu  | -            | `{"id_peminjaman": 12,  "id_anggota": 5,  "id_petugas": 2, "id_buku":1, "jml_buku":3,  "tgl_pinjam": "2025-09-02",  "tgl_kembali": null,  "status": "dipinjam"}` | Anggota dan petugas |
| POST        | /peminjaman                | Membuat data peminjaman baru            | `{ "id_anggota": 1, "id_petugas": 2, "id_buku":1, "jml_buku":3, "tanggal_pinjam": "2025-09-01", "tanggal_jatuh_tempo": "2025-09-15", "status": "dipinjam" }` | Data peminjaman baru | Petugas only |
| PUT         | /peminjaman/{id_peminjaman}| Update data peminjaman tertentu         | `{ "Tgl-kembali":"2025-09-03","status": "dikembalikan" }` | `{"id_peminjaman": 12,  "id_anggota": 5,  "id_petugas": 2, "id_buku":1, "jml_buku":3,  "tgl_pinjam": "2025-09-02",  "tgl_kembali": 2025-09-03,  "status": "dikembalikan"}` | Petugas only |
| DELETE      | /peminjaman/{id_peminjaman}| Hapus data peminjaman tertentu          | -            | `{"message": Data peminjaman dengan id 1 berhasil dihapus"}` | Petugas only |

---

## Pengembalian

| HTTP Method | URL Path                        | Kegunaan                               | Request Body | Expected Response | Butuh Auth |
|-------------|---------------------------------|----------------------------------------|--------------|------------------|------------|
| GET         | /pengembalian                   | Mendapatkan daftar pengembalian         | -            | `{"id_pengembalian": 1, "id_peminjaman": 5, "tgl_kembali": "2025-09-01", "denda": 5000.00}` | Anggota dan petugas |
| GET         | /pengembalian/{id_pengembalian} | Mendapatkan detail pengembalian tertentu| -            | `{"id_pengembalian": 1, "id_peminjaman": 5, "tgl_kembali": "2025-09-01", "denda": 5000.00}` | Anggota dan petugas |
| POST        | /pengembalian                   | Membuat data pengembalian baru          | `{ "id_peminjaman": 1, "tanggal_kembali": "2025-09-01", "denda": 5000 }` | Data pengembalian baru | petugas |
| PUT         | /pengembalian/{id_pengembalian} | Update data pengembalian tertentu       | `{ "denda": 10000 }` | `{"id_pengembalian": 1, "id_peminjaman": 5, "tgl_kembali": "2025-09-01", "denda": 10000}` | Petugas only |
| DELETE      | /pengembalian/{id_pengembalian} | Hapus data pengembalian tertentu        | -            | `{"message": Data pengembalian dengan id 1 berhasil dihapus"}` | Petugas only |

---
