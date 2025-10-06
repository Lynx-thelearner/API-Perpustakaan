import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from httpx import AsyncClient, ASGITransport
from main import app

@pytest.mark.asyncio
async def test_create_kategori(auth_header):
    transport = ASGITransport(app=app)
    payload = {
        "nama_kategori": "Fiksi"
    }
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Endpoint buat create kategori
        response = await ac.post("/kategori/", json=payload, headers=auth_header)
        
    assert response.status_code == 200
    data = response.json()
    
    assert data["nama_kategori"] == payload["nama_kategori"]
    assert "id_kategori" in data
    
@pytest.mark.asyncio
async def test_get_all_kategori():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Endpoint buat get all kategori
        response = await ac.get("/kategori/")
        
    assert response.status_code == 200
    data = response.json()
    
    # Kita buat pake list lagi
    assert isinstance(data, list)
    # Paling enggak ada 1 kategori
    assert len(data) >= 1
    # Cek field yang di return
    assert "id_kategori" in data[0]
    assert "nama_kategori" in data[0]
    
@pytest.mark.asyncio
async def test_get_kategori_by_id(auth_header):
    transport = ASGITransport(app=app)
    # Pertama, kita buat kategori dulu
    payload = {
        "nama_kategori": "Non-Fiksi"
    }
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        create_response = await ac.post("/kategori/", json=payload, headers=auth_header)
        
    assert create_response.status_code == 200
    created_data = create_response.json()
    kategori_id = created_data["id_kategori"]
    
    # Sekarang kita coba get kategori by id
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.get(f"/kategori/{kategori_id}")
        
    assert response.status_code == 200
    data = response.json()
    
    assert data["id_kategori"] == kategori_id
    assert data["nama_kategori"] == payload["nama_kategori"]    
    
@pytest.mark.asyncio
async def test_update_kategori(auth_header):
    transport = ASGITransport(app=app)
    # Pertama, kita buat kategori dulu
    payload = {
        "nama_kategori": "Sejarah"
    }
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        create_response = await ac.post("/kategori/", json=payload, headers=auth_header)
        
    assert create_response.status_code == 200
    created_data = create_response.json()
    kategori_id = created_data["id_kategori"]
    
    # Sekarang kita coba update kategori
    update_payload = {
        "nama_kategori": "Biografi"
    }
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.patch(f"/kategori/{kategori_id}", json=update_payload, headers=auth_header)
        
    assert response.status_code == 200
    data = response.json()
    
    assert data["id_kategori"] == kategori_id
    assert data["nama_kategori"] == update_payload["nama_kategori"]
    
@pytest.mark.asyncio
async def test_delete_kategori(auth_header):
    transport = ASGITransport(app=app)
    #Buat kategori dulu yang bakal dihapus
    payload = {
        "nama_kategori": "Horror"
    }
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        create_response = await ac.post("/kategori/", json=payload, headers=auth_header)
    assert create_response.status_code == 200
    created_data = create_response.json()
    kategori_id = created_data["id_kategori"]
    
    #Hapus kategori yang tadi dibuat    
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.delete(f"/kategori/{kategori_id}", headers=auth_header)
    assert response.status_code == 200
    del_response = response.json()
    nama_kategori = payload["nama_kategori"]
    assert del_response["message"] == f"Kategori {nama_kategori} berhasil dihapus"
    
    #Coba get kategori yang sudah dihapus
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        get_response = await ac.get(f"/kategori/{kategori_id}")
    assert get_response.status_code == 404
    err_response = get_response.json()
    assert err_response["detail"] == "Kategori not found"