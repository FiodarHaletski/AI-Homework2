import pytest
from httpx import AsyncClient
from main import app
import asyncio

@pytest.mark.asyncio
async def test_register_and_login():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Register
        resp = await ac.post("/users/", json={
            "name": "Test User",
            "username": "testuser",
            "email": "test@example.com",
            "password": "testpass",
            "address": {
                "street": "Test St",
                "suite": "Apt 1",
                "city": "Testville",
                "zipcode": "00000",
                "geo": {"lat": "0", "lng": "0"}
            },
            "phone": "1234567890",
            "website": "test.com",
            "company": {
                "name": "TestCo",
                "catchPhrase": "Test phrase",
                "bs": "test bs"
            }
        })
        assert resp.status_code == 200
        # Login
        resp = await ac.post("/token", data={"username": "test@example.com", "password": "testpass"})
        assert resp.status_code == 200
        token = resp.json()["access_token"]
        # Get users (protected)
        resp = await ac.get("/users/", headers={"Authorization": f"Bearer {token}"})
        assert resp.status_code == 200
        assert any(u["email"] == "test@example.com" for u in resp.json())
        # Update user
        user_id = [u["id"] for u in resp.json() if u["email"] == "test@example.com"][0]
        resp = await ac.put(f"/users/{user_id}", json={
            "name": "Test User2",
            "username": "testuser2",
            "email": "test2@example.com",
            "address": {
                "street": "Test St2",
                "suite": "Apt 2",
                "city": "Testville2",
                "zipcode": "00001",
                "geo": {"lat": "1", "lng": "1"}
            },
            "phone": "0987654321",
            "website": "test2.com",
            "company": {
                "name": "TestCo2",
                "catchPhrase": "Test phrase2",
                "bs": "test bs2"
            }
        }, headers={"Authorization": f"Bearer {token}"})
        assert resp.status_code == 200
        # Delete user
        resp = await ac.delete(f"/users/{user_id}", headers={"Authorization": f"Bearer {token}"})
        assert resp.status_code == 204 