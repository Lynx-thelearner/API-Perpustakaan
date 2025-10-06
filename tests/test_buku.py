import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from httpx import AsyncClient, ASGITransport
from main import app

@pytest.mark.asyncio 
async def test_create_buku(auth_header):
    transport = ASGITransport(app=app)
    payload = {
        "judul": "Belajar FastAPI",
        "pengarang": "Jane Doe",
        "penerbit": "Tech Books",
        "tahun_terbit": 2023,
        "stok": 10,
        "id_kategori": 1
    }
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Endpoint buat create buku
        response = await ac.post("/buku/", json=payload, headers=auth_header)
        
    assert response.status_code == 200
    data = response.json()
    
    assert data["judul"] == payload["judul"]
    assert data["pengarang"] == payload["pengarang"]
    assert data["penerbit"] == payload["penerbit"]
    assert data["tahun_terbit"] == payload["tahun_terbit"]
    assert data["stok"] == payload["stok"]
    assert data["id_kategori"] == payload["id_kategori"]
    assert "id_buku" in data
    
@pytest.mark.asyncio
async def test_get_all_buku():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Endpoint buat get all buku
        response = await ac.get("/buku/")
        
    assert response.status_code == 200
    data = response.json()
    
    # Kita buat pake list
    assert isinstance(data, list)
    # Paling enggak ada 1 buku
    assert len(data) >= 1
    # Cek field yang di return
    assert "id_buku" in data[0]
    assert "judul" in data[0]
    assert "pengarang" in data[0]
    assert "penerbit" in data[0]
    assert "tahun_terbit" in data[0]
    assert "stok" in data[0]
    assert "id_kategori" in data[0]
    
@pytest.mark.asyncio
async def test_get_buku_by_id(auth_header):
    transport = ASGITransport(app=app)
    # Pertama, kita buat buku dulu
    payload = {
        "judul": "Belajar FastAPI",
        "pengarang": "Jane Doe",
        "penerbit": "Tech Books",
        "tahun_terbit": 2023,
        "stok": 10,
        "id_kategori": 2
    }
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        create_response = await ac.post("/buku/", json=payload, headers=auth_header)
        assert create_response.status_code == 200
        created_buku = create_response.json()
        buku_id = created_buku["id_buku"]
        
        # Sekarang get buku berdasarkan ID
        get_response = await ac.get(f"/buku/{buku_id}")
        
    assert get_response.status_code == 200
    data = get_response.json()
    
    assert data["id_buku"] == buku_id
    assert data["judul"] == payload["judul"]
    assert data["pengarang"] == payload["pengarang"]
    assert data["penerbit"] == payload["penerbit"]
    assert data["tahun_terbit"] == payload["tahun_terbit"]
    assert data["stok"] == payload["stok"]
    assert data["id_kategori"] == payload["id_kategori"]
    
@pytest.mark.asyncio
async def test_update_buku(auth_header):
    transport = ASGITransport(app=app)
    #Buat buku, kek function sebelumnya
    payload = {
        "judul": "Belajar FastAPI",
        "pengarang": "Jane Doe",
        "penerbit": "Tech Books",
        "tahun_terbit": 2023,
        "stok": 10,
        "id_kategori": 2
    }
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        create_response = await ac.post("/buku/", json=payload, headers=auth_header)
        assert create_response.status_code == 200
        created_buku = create_response.json()
        buku_id = created_buku["id_buku"]
        
        #Ini buat update buku
        
        update_payload = {
            "judul": "Mastering FastAPI",
            "stok": 15
        }
        
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as ac:
            response = await ac.patch(f"/buku/{buku_id}", json=update_payload, headers=auth_header)
            assert response.status_code == 200
            data = response.json()
            
            #ngecek data yang di update
            assert data["id_buku"] == buku_id
            assert data["judul"] == update_payload["judul"]
            assert data["stok"] == update_payload["stok"]
            
            # Field lain harusnya tetap sama
            assert data["pengarang"] == payload["pengarang"]
            assert data["penerbit"] == payload["penerbit"]
            assert data["tahun_terbit"] == payload["tahun_terbit"]
            assert data["id_kategori"] == payload["id_kategori"]
            
@pytest.mark.asyncio
async def test_delete_buku(auth_header):
    transport = ASGITransport(app=app)
    
    #Buat buku lagi buat dihapus
    payload = {
        "judul": "Belajar FastAPI",
        "pengarang": "Jane Doe",
        "penerbit": "Tech Books",
        "tahun_terbit": 2023,
        "stok": 10,
        "id_kategori": 2
    }
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        create_res = await ac.post("/buku/", json=payload, headers=auth_header)
        assert create_res.status_code == 200
        created_buku = create_res.json()
        buku_id = created_buku["id_buku"]
        
        #delete buku
        del_response = await ac.delete(f"/buku/{buku_id}", headers=auth_header)
        assert del_response.status_code == 200
        assert del_response.json()["message"] == f"Buku dengan id {buku_id} berhasil dihapus"
        
        # Cek apa bukunya masih ada?
        get_response = await ac.get(f"/buku/{buku_id}")
        assert get_response.status_code == 404
        error_data = get_response.json()
        assert error_data["detail"] == "Buku tidak ditemukan"
    