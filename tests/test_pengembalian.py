import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from httpx import AsyncClient, ASGITransport
from main import app
from decimal import Decimal

@pytest.mark.asyncio
async def test_create_pengembalian(auth_header):
    transport = ASGITransport(app=app)
    #buat data peminjaman dulu
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
        response = await ac.post("/peminjaman/", json=payload, headers=auth_header)
        assert response.status_code == 200
    data = response.json()
    id_peminjaman = data["id_peminjaman"]
    
    #buat data pengembalian
    payload_kembali = {
        "id_peminjaman": id_peminjaman,
        "tgl_kembali": "2024-10-09",
        "denda": 0,
    }
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Endpoint buat create pengembalian
        response = await ac.post("/pengembalian/", json=payload_kembali, headers=auth_header)
        assert response.status_code == 200
    data = response.json()
    assert data["id_peminjaman"] == payload_kembali["id_peminjaman"]
    assert data["tgl_kembali"] == payload_kembali["tgl_kembali"]
    assert Decimal(data["denda"]) == payload_kembali["denda"]

@pytest.mark.asyncio
async def test_get_all_pengembalian(auth_header):
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test", headers=auth_header) as ac:
        # Endpoint buat get all pengembalian
        response = await ac.get("/pengembalian/")
        
    assert response.status_code == 200
    data = response.json()
    
    # Kita buat pake list
    assert isinstance(data, list)
    # Paling enggak ada 1 pengembalian
    assert len(data) >= 1
    # Cek field yang di return
    assert "id_pengembalian" in data[0]
    assert "id_peminjaman" in data[0]
    assert "tgl_kembali" in data[0]
    assert "denda" in data[0]
    
@pytest.mark.asyncio
async def test_get_pengembalian_by_id(auth_header):
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
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/peminjaman/", json=payload, headers=auth_header)
        assert response.status_code == 200
    data = response.json()
    id_peminjaman = data["id_peminjaman"]
    
    #buat data pengembalian
    payload_kembali = {
        "id_peminjaman": id_peminjaman,
        "tgl_kembali": "2024-10-09",
        "denda": 0,
    }
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/pengembalian/", json=payload_kembali, headers=auth_header)
        assert response.status_code == 200
    data = response.json()
    id_pengembalian = data["id_pengembalian"]
    
    # Baru kita test get by id pengembalian
    async with AsyncClient(transport=transport, base_url="http://test", headers=auth_header) as ac:
        # Endpoint buat get pengembalian by id
        response = await ac.get(f"/pengembalian/{id_pengembalian}")
    assert response.status_code == 200
    data = response.json()
    
    assert data["id_peminjaman"] == payload_kembali["id_peminjaman"]
    assert data["tgl_kembali"] == payload_kembali["tgl_kembali"]
    assert Decimal(data["denda"]) == payload_kembali["denda"]
    
@pytest.mark.asyncio
async def test_update_pengembalian(auth_header):
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
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/peminjaman/", json=payload, headers=auth_header)
        assert response.status_code == 200
    data = response.json()
    id_peminjaman = data["id_peminjaman"]
    
    #buat data pengembalian
    payload_kembali = {
        "id_peminjaman": id_peminjaman,
        "tgl_kembali": "2024-10-09",
        "denda": 0,
    }
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/pengembalian/", json=payload_kembali, headers=auth_header)
        assert response.status_code == 200
    data = response.json()
    id_pengembalian = data["id_pengembalian"]
    
    # Baru kita test update pengembalian
    update_payload = {
        "tgl_kembali": "2024-10-11",
        "denda": 5000,
    }
    async with AsyncClient(transport=transport, base_url="http://test", headers=auth_header) as ac:
        # Endpoint buat update pengembalian by id
        response = await ac.patch(f"/pengembalian/{id_pengembalian}", json=update_payload)
    assert response.status_code == 200
    data = response.json()
    
    assert data["id_peminjaman"] == payload_kembali["id_peminjaman"]
    assert data["tgl_kembali"] == update_payload["tgl_kembali"]
    assert Decimal(data["denda"]) == update_payload["denda"]
    
@pytest.mark.asyncio
async def test_hapus_pengembalian(auth_header):
    transport = ASGITransport(app=app)
    #Buat data peminjaman dulu
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
        response = await ac.post("/peminjaman/", json=payload, headers=auth_header)
        assert response.status_code == 200
    data = response.json()
    id_peminjaman = data["id_peminjaman"]
    
    #buat data pengembalian
    payload_kembali = {
        "id_peminjaman": id_peminjaman,
        "tgl_kembali": "2024-10-09",
        "denda": 0,
    }
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("/pengembalian/", json=payload_kembali, headers=auth_header)
        assert response.status_code == 200
    data = response.json()
    id_pengembalian = data["id_pengembalian"]
    
    # Baru kita test hapus pengembalian
    async with AsyncClient(transport=transport, base_url="http://test", headers=auth_header) as ac:
        # Endpoint buat delete pengembalian by id
        response = await ac.delete(f"/pengembalian/{id_pengembalian}")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == f"Pengembalian dengan id {id_pengembalian} telah dihapus"