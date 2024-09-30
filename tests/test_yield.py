from fastapi.testclient import TestClient
from app.main import app
from app.db.database import get_db, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import pytest
from datetime import date

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

def test_create_yield():
    # First, create a crop
    crop_response = client.post(
        "/api/v1/crops/",
        json={"name": "Wheat", "variety": "Winter Wheat", "planting_date": "2023-10-01", "expected_harvest_date": "2024-07-15", "field_size": 100.5},
    )
    crop_id = crop_response.json()["id"]

    # Now, create a yield for this crop
    response = client.post(
        "/api/v1/yields/",
        json={"crop_id": crop_id, "harvest_date": "2024-07-20", "quantity": 500.5, "quality": 95.0},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["crop_id"] == crop_id
    assert "id" in data

def test_read_yield():
    response = client.get("/api/v1/yields/1")
    assert response.status_code == 200
    data = response.json()
    assert data["quantity"] == 500.5

def test_update_yield():
    response = client.put(
        "/api/v1/yields/1",
        json={"crop_id": 1, "harvest_date": "2024-07-21", "quantity": 550.0, "quality": 97.0},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["quantity"] == 550.0

def test_delete_yield():
    response = client.delete("/api/v1/yields/1")
    assert response.status_code == 200
    
    response = client.get("/api/v1/yields/1")
    assert response.status_code == 404

def test_get_yields_by_crop():
    response = client.get("/api/v1/crops/1/yields")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data[0]["crop_id"] == 1

@pytest.fixture(autouse=True)
def run_around_tests():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)