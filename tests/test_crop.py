from fastapi.testclient import TestClient
from app.main import app
from app.db.database import get_db, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_create_crop():
    response = client.post(
        "/api/v1/crops/",
        json={"name": "Wheat", "variety": "Winter Wheat", "planting_date": "2023-10-01", "expected_harvest_date": "2024-07-15", "field_size": 100.5},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Wheat"
    assert "id" in data

def test_read_crop():
    response = client.get("/api/v1/crops/1")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Wheat"

def test_update_crop():
    response = client.put(
        "/api/v1/crops/1",
        json={"name": "Wheat", "variety": "Spring Wheat", "planting_date": "2023-03-01", "expected_harvest_date": "2023-08-15", "field_size": 120.0},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["variety"] == "Spring Wheat"

def test_delete_crop():
    response = client.delete("/api/v1/crops/1")
    assert response.status_code == 200
    
    response = client.get("/api/v1/crops/1")
    assert response.status_code == 404

@pytest.fixture(autouse=True)
def run_around_tests():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)