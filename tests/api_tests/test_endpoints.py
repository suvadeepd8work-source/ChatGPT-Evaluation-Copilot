import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from phase3_backend.main import app
from phase3_backend.models.base import Base, get_db
import os

# Setup test database
SQLALCHEMY_DATABASE_URL = "sqlite:///./test_api.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

@pytest.fixture(scope="module")
def client():
    Base.metadata.create_all(bind=engine)
    with TestClient(app) as c:
        yield c
    Base.metadata.drop_all(bind=engine)
    if os.path.exists("./test_api.db"):
        os.remove("./test_api.db")

def test_read_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Phase 3 API is running" in response.json()["message"]

def test_create_session(client):
    response = client.post("/api/v1/sessions/create", params={"user_id": "test_user"})
    assert response.status_code == 200
    assert "session_id" in response.json()
    assert response.json()["user_id"] == "test_user"

def test_process_evaluation_missing_data(client):
    # Test with invalid data
    response = client.post("/api/v1/evaluation/process", json={"prompt": ""})
    # Depending on pydantic validation, this might be 422 or handled by service
    assert response.status_code in [422, 500]

def test_log_verification(client):
    # First create a session/interaction (mocking interaction_id for now or using a real one)
    interaction_id = "test-interaction-123"
    response = client.post(
        f"/api/v1/evaluation/verify/{interaction_id}", 
        json={"type": "link_click", "details": {"url": "http://example.com"}}
    )
    assert response.status_code == 200
    assert response.json()["action_type"] == "link_click"
