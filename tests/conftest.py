import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import pytest, pytest_asyncio
from httpx import AsyncClient, ASGITransport
from main import app

#Fixture untuk async client
@pytest_asyncio.fixture
async def client():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac
        
# Fixture untuk token JWT
@pytest_asyncio.fixture
async def auth_header():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        login_data = {
            "username": "diazpetugas",
            "password": "12345678"
        }
        res = await ac.post("/auth/login", data=login_data)
        assert res.status_code == 200, res.text
        token = res.json().get("access_token")
        return {"Authorization": f"Bearer {token}"}
