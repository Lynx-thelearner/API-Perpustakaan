import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from httpx import AsyncClient, ASGITransport
from main import app

@pytest.mark.asyncio
async def test_create_peminjaman(auth_header):
    transport = ASGITransport(app=app)
    payload = {
        "id_user": 11,  # Pastikan user ini adalah anggota
        "id_buku": 1,  # Pastikan buku ini ada dan stoknya cukup
        "id_petugas": 9,  # Pastikan user ini adalah petugas
        "jumlah": 1,
        "tgl_pinjam": "2024-10-01",
        "tgl_kembali": "2024-10-10",
        "status": "dipinjam"
    }
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Endpoint buat create peminjaman
        response = await ac.post("/peminjaman/", json=payload, headers=auth_header)
        assert response.status_code == 200
    data = response.json()
    assert data["id_user"] == payload["id_user"]
    assert data["id_buku"] == payload["id_buku"]
    assert data["id_petugas"] == payload["id_petugas"]
    assert data["jumlah"] == payload["jumlah"]
    assert data["tgl_pinjam"] == payload["tgl_pinjam"]
    assert data["tgl_kembali"] == payload["tgl_kembali"]
    assert data["status"] == payload["status"]
    
@pytest.mark.asyncio
async def test_get_all_peminjaman(auth_header):
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test", headers=auth_header) as ac:
        # Endpoint buat get all peminjaman
        response = await ac.get("/peminjaman/")
        
    assert response.status_code == 200
    data = response.json()
    
    # Kita buat pake list
    assert isinstance(data, list)
    # Paling enggak ada 1 peminjaman
    assert len(data) >= 1
    # Cek field yang di return
    assert "id_peminjaman" in data[0]
    assert "id_user" in data[0]
    assert "id_buku" in data[0]
    assert "id_petugas" in data[0]
    assert "jumlah" in data[0]
    assert "tgl_pinjam" in data[0]
    assert "tgl_kembali" in data[0]
    assert "status" in data[0]
    
@pytest.mark.asyncio
async def test_get_peminjaman_by_id(auth_header):
    transport = ASGITransport(app=app)
    # Pertama, kita buat peminjaman dulu
    payload = {
        "id_user": 23,  # Pastikan user ini adalah anggota
        "id_buku": 11,  # Pastikan buku ini ada dan stoknya cukup
        "id_petugas": 10,  # Pastikan user ini adalah petugas
        "jumlah": 1,
        "tgl_pinjam": "2024-10-01",
        "tgl_kembali": "2024-10-10",
        "status": "dipinjam"
    }
    async with AsyncClient(transport=transport, base_url="http://test", headers=auth_header) as ac:
        create_response = await ac.post("/peminjaman/", json=payload)
        assert create_response.status_code == 200
    created_data = create_response.json()
    peminjaman_id = created_data["id_peminjaman"]
    
    # Sekarang kita coba get peminjaman by id
    async with AsyncClient(transport=transport, base_url="http://test", headers=auth_header) as ac:
        response = await ac.get(f"/peminjaman/{peminjaman_id}")

    assert response.status_code == 200
    data = response.json()
    
    assert data["id_peminjaman"] == peminjaman_id
    assert data["id_user"] == payload["id_user"]
    assert data["id_buku"] == payload["id_buku"]
    assert data["id_petugas"] == payload["id_petugas"]
    assert data["jumlah"] == payload["jumlah"]
    assert data["tgl_pinjam"] == payload["tgl_pinjam"]
    assert data["tgl_kembali"] == payload["tgl_kembali"]
    assert data["status"] == payload["status"]
    
@pytest.mark.asyncio
async def test_update_peminjaman(auth_header):
    transport = ASGITransport(app=app)
    #Buat data  peminjaman yang mau diubah
    payload = {
        "id_user": 12,  # Pastikan user ini adalah anggota
        "id_buku": 12,  # Pastikan buku ini ada dan stoknya cukup
        "id_petugas": 10,  # Pastikan user ini adalah petugas
        "jumlah": 1,
        "tgl_pinjam": "2024-10-01",
        "tgl_kembali": "2024-10-10",
        "status": "dipinjam"
    }
    async with AsyncClient(transport=transport, base_url="http://test", headers=auth_header) as ac:
        create_response = await ac.post("/peminjaman/", json=payload)
        assert create_response.status_code == 200
    created_data = create_response.json()
    peminjaman_id = created_data["id_peminjaman"]
    
    #Update Peminjamannya
    update_payload = {
        "status": "dikembalikan",
        "tgl_kembali": "2024-10-05"
    }
    async with AsyncClient(transport=transport, base_url="http://test", headers=auth_header) as ac:
        update_response = await ac.patch(f"/peminjaman/{peminjaman_id}", json=update_payload)
        
        assert update_response.status_code == 200
        data = update_response.json()
        
        assert data["id_peminjaman"] == peminjaman_id
        assert data["status"] == update_payload["status"]
        assert data["tgl_kembali"] == update_payload["tgl_kembali"]
        # Field lain harusnya tetap
        assert data["id_user"] == payload["id_user"]
        assert data["id_buku"] == payload["id_buku"]
        assert data["id_petugas"] == payload["id_petugas"]
        assert data["jumlah"] == payload["jumlah"]
        assert data["tgl_pinjam"] == payload["tgl_pinjam"]

@pytest.mark.asyncio
async def test_hapus_peminjaman(auth_header):
    transport = ASGITransport(app=app)
    #Buat data  peminjaman yang mau dihapus
    payload = {
        "id_user": 32,  # Pastikan user ini adalah anggota
        "id_buku": 13,  # Pastikan buku ini ada dan stoknya cukup
        "id_petugas": 10,  # Pastikan user ini adalah petugas
        "jumlah": 1,
        "tgl_pinjam": "2024-10-01",
        "tgl_kembali": "2024-10-10",
        "status": "dipinjam"
    }
    async with AsyncClient(transport=transport, base_url="http://test", headers=auth_header) as ac:
        create_response = await ac.post("/peminjaman/", json=payload)
        assert create_response.status_code == 200
    created_data = create_response.json()
    peminjaman_id = created_data["id_peminjaman"]
    
    #Tinggal hapus peminjamannya
    async with AsyncClient(transport=transport, base_url="http://test", headers=auth_header) as ac:
        del_response = await ac.delete(f"/peminjaman/{peminjaman_id}")
    assert del_response.status_code == 200
    del_data = del_response.json()
    assert del_data["message"] == f"Peminjaman dengan id {peminjaman_id} berhasil dihapus"