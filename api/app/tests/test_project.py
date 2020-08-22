from app.models.project import Project


def test_post_project(client, test_db_session):
    data = {
        "title": "Test",
        "description": "Test description",
        "owner_id": "1",
    }
    response = client.post("/projects", json=data)
    assert response.status_code == 200
    assert response.json() == {
        "title": "Test",
        "description": "Test description",
        "owner_id": 1,
        "id": 1,
    }


def test_get_project(client, test_db_session):
    project = Project(title="Test", description="Test description", owner_id="1",)
    test_db_session.add(project)
    test_db_session.commit()
    response = client.get("/projects/1")
    assert response.status_code == 200
    assert response.json() == {
        "title": "Test",
        "description": "Test description",
        "owner_id": 1,
        "id": 1,
    }
