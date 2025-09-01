| HTTP Method | URL Path | Kegunaan | Request Body | Expected Response | Butuh auth |
|-------------|----------|----------|--------------|------------------|------------|
| GET | /anggota | Untuk mendapatkan daftar anggota | - | `[{"id":1,"nama":"Diaz","email":"diaz@example.com"}]` | Yes |
| GET | /anggota/{id} | Untuk mendapatkan detail anggota tertentu | - | `{"id":1,"nama":"Diaz","email":"diaz@example.com"}` | Yes |
| POST | /anggota | Untuk menambahkan anggota baru | `{"nama":"Diaz","email":"diaz@example.com","alamat":"Samarinda"}` | `{"message":"Anggota berhasil ditambahkan"}` | No |
| PUT | /anggota/{id} | Untuk mengupdate data anggota | `{"nama":"Diaz Update","email":"diaz@example.com"}` | `{"message":"Anggota berhasil diupdate"}` | Yes |
| DELETE | /anggota/{id} | Untuk menghapus anggota | - | `{"message":"Anggota berhasil dihapus"}` | Yes |
| GET | /buku | Untuk mendapatkan daftar buku | - | `[{"id":1,"judul":"Laskar Pelangi","penulis":"Andrea Hirata"}]` | Yes |
| GET | /buku/{id} | Untuk mendapatkan detail buku | - | `{"id":1,"judul":"Laskar Pelangi","penulis":"Andrea Hirata"}` | Yes |
| POST | /buku | Untuk menambahkan buku baru | `{"judul":"Laskar Pelangi","penulis":"Andrea Hirata","stok":10}` | `{"message":"Buku berhasil ditambahkan"}` | Yes |
| PUT | /buku/{id} | Untuk mengupdate data buku | `{"stok":15}` | `{"message":"Buku berhasil diupdate"}` | Yes |
| DELETE | /buku/{id} | Untuk menghapus buku | - | `{"message":"Buku berhasil dihapus"}` | Yes |
| POST | /peminjaman | Untuk membuat transaksi peminjaman | `{"id_anggota":1,"id_buku":[1,2],"tgl_pinjam":"2025-09-01"}` | `{"message":"Peminjaman berhasil dibuat"}` | Yes |
| PUT | /pengembalian/{id} | Untuk mengembalikan buku | `{"tgl_kembali":"2025-09-10","denda":5000}` | `{"message":"Pengembalian berhasil diproses"}` | Yes |
