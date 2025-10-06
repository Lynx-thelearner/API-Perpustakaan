

@pytest.mark.asyncio
@pytest.mark.parametrize("payload", [
    {
        "nama": "John Doe",
        "username": "johndoe",
        "alamat": "123 Main St",
        "no_telp": "+6281234567890",
        "email": "user@example.com",
        "role": "anggota",
        "password": "securepassword"
    },
    {
        "nama": "Jane Smith",
        "username": "janesmith",
        "alamat": "456 Elm St",
        "no_telp": "081234567890",
        "email": "user2@example.com",
        "role": "petugas",
        "password": "anothersecurepassword"
    }
])
async def test_create_user(payload, auth_header):
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        #Endpoint buat create user admin
        response = await ac.post("/user/", json=payload,headers=auth_header)
        
    assert response.status_code == 200
    data = response.json()
    
    assert data["nama"] == payload["nama"]
    assert data["username"] == payload["username"]
    assert data["alamat"] == payload["alamat"]
    assert data["no_telp"] == payload["no_telp"]
    assert data["email"] == payload["email"]
    assert data["role"] == payload["role"]
    assert "password" not in data
    
@pytest.mark.asyncio
async def test_get_all_user(auth_header):
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        #Endpoint buat get all user
        response = await ac.get("/user/", headers=auth_header)
        assert response.status_code == 200
        data = response.json()
        
        #Kita buat pake list
        assert isinstance(data, list)
        #Paling enggak ada 1 user
        assert len(data) >= 1
        #cek field yang di return
        assert "id_user" in data[0]
        assert "username" in data[0]
        assert "email" in data[0]
        
@pytest.mark.asyncio
async def test_get_user_by_id(auth_header):
    transport = ASGITransport(app=app)
    #Buat data user dulu
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {
            "nama": "Test User",
            "username": "testuser",
            "alamat": "321 Pine St",
            "no_telp": "+6281122334455",
            "email": "testing@gmail.com",
            "password": "testpassword"
        }
        create_res = await ac.post("/user/register", json=payload, headers=auth_header)
        assert create_res.status_code == 200
        created_user = create_res.json()
        user_id = created_user["id_user"]
        
        #Endpoint buat get user by id
        response = await ac.get(f"/user/{user_id}", headers=auth_header)
        assert response.status_code == 200
        data = response.json()
        
        assert data["id_user"] == user_id
        assert data["username"] == payload["username"]
        assert data["email"] == payload["email"]
        
@pytest.mark.asyncio
async def test_register():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        # Endpoint for user registration
        payload = {
            "nama": "New User",
            "username": "newuser",
            "alamat": "789 Oak St",
            "no_telp": "+6289876543210",
            "email": "newuser@example.com",
            "password": "newsecurepassword"
        }
        response = await ac.post("/user/register", json=payload)
        assert response.status_code == 200
        data = response.json()
        
        #ngecek data yang di return
        assert data["nama"] == payload["nama"]
        assert data["username"] == payload["username"]
        assert data["alamat"] == payload["alamat"]
        assert data["email"] == payload["email"]
        assert "password" not in data
        
        
@pytest.mark.asyncio
async def test_update_user(auth_header):
    transport = ASGITransport(app=app)
    #Buat data user sebelum update
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        payload = {
            "nama": "Alice Wonderland",
            "username": "alicewonder",
            "alamat": "654 Maple St",
            "no_telp": "+6289988776655",
            "email": "alicewonderland@gmail.com",
            "password": "alicepassword",
            "role": "anggota"
        }
        
        created_res = await ac.post("/user/", json=payload, headers=auth_header)
        assert created_res.status_code == 200
        created_user = created_res.json()
        user_id = created_user["id_user"]
        
        #Payload buat update
        update_payload = {
            "nama": "Alice Updated",
            "alamat": "Updated Address",
            "no_telp": "+6281122334455"
        }
        
        transport = ASGITransport(app=app)
        async with AsyncClient(transport=transport, base_url="http://test") as ac:
            response = await ac.patch(f"/user/{user_id}", json=update_payload, headers=auth_header)
            assert response.status_code == 200
            data = response.json()
            
            #ngecek data yang di update
            assert data["id_user"] == user_id
            assert data["nama"] == update_payload["nama"]
            assert data["alamat"] == update_payload["alamat"]
            assert data["no_telp"] == update_payload["no_telp"]
            
            #Field yang tidak di update harusnya tetap sama
            assert data["username"] == payload["username"]
            assert data["email"] == payload["email"]
            assert data["role"] == payload["role"]
            assert "password" not in data
            
@pytest.mark.asyncio
async def test_delete_user(auth_header):
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        #Buat data user yang mau di delete
        payload = {
            "nama": "Bob Builder",
            "username": "bobbuilder",
            "alamat": "987 Birch St",
            "no_telp": "+6282233445566",
            "email": "bob@gmail.com",
            "password": "bobpassword",
            "role": "petugas"
        }
        create_res = await ac.post("/user/", json=payload, headers=auth_header)
        assert create_res.status_code == 200
        created_user = create_res.json()
        user_id = created_user["id_user"]
        
        #Delete usernya
        delete_res = await ac.delete(f"/user/{user_id}", headers=auth_header)
        assert delete_res.status_code == 200
        assert delete_res.json()["message"] == f"user dengan id {user_id} berhasil dihapus"
        
        #Ini buat ngecek apa masih ada usernya? 
        get_res = await ac.get(f"/user/{user_id}", headers=auth_header)
        assert get_res.status_code == 404