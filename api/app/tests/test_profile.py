from app.models.profile import Profile


def test_post_profile(client, test_db_session):
    data = {
        "name": "Ahmed",
        "email": "Ahmed@gmail.com",
        "address": "Stockholm",
        "birthdate": "1933-01-01",
        "about_me": "Hi im Ahmed",
        "telephone_number": "2131241",
    }
    response = client.post("/profiles", json=data)
    assert response.status_code == 200
    assert response.json() == {
        "name": "Ahmed",
        "email": "Ahmed@gmail.com",
        "address": "Stockholm",
        "birthdate": "1933-01-01",
        "about_me": "Hi im Ahmed",
        "telephone_number": "2131241",
        "id": 1,
        "projects": [],
    }


def test_get_profile(client, test_db_session):
    profile = Profile(
        name="Ahmed",
        email="Ahmed@gmail.com",
        address="Stockholm",
        birthdate="1933-01-01",
        about_me="Hi im Ahmed",
        telephone_number="2131241",
    )
    test_db_session.add(profile)
    test_db_session.commit()
    response = client.get("/profiles/1")
    assert response.status_code == 200
    assert response.json() == {
        "name": "Ahmed",
        "email": "Ahmed@gmail.com",
        "address": "Stockholm",
        "birthdate": "1933-01-01",
        "about_me": "Hi im Ahmed",
        "telephone_number": "2131241",
        "id": 1,
        "projects": [],
    }
