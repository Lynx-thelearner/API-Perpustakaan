import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest
from httpx import AsyncClient, ASGITransport
from main import app

@pytest.mark.asyncio
async def test_login_success():
    transport = ASGITransport(app=app)
    payload = {
        "username": "diazpetugas",
        "password": "12345678"
    }
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("auth/login", data=payload)
        
    assert response.status_code == 200
    data = response.json()
    
    assert "access_token" in data
    assert data["token_type"] == "bearer"
    
@pytest.mark.asyncio
async def test_login_failure():
    transport = ASGITransport(app=app)
    payload = {
        "username": "diazpetugas",
        "password": "wrongpassword"
    }
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        response = await ac.post("auth/login", data=payload)
        
    assert response.status_code == 401
    data = response.json()
    
    assert data["detail"] == "Incorrect username or password"