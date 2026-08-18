from fastapi.testclient import TestClient
from main_3 import app

client = TestClient(app)

def test_get_developers():
    response = client.get('/developers')
    assert response.status_code ==200

def test_get_developer():
    response = client.get('/developers/69b45bc6364e64aad5575bba')
    assert response.status_code ==200

def test_get_developer_skills():
    response = client.get('/developers/69b45bc6364e64aad5575bba/skills')
    assert response.status_code ==200

def test_get_developer_experience():
    response = client.get('/developers/69b45bc6364e64aad5575bba/experience')
    assert response.status_code ==200

def test_create_developer_experience():
    response = client.post('/developers', json={
        "id": 3,
        "name": "Luis Mendoza",
        "country": "Peru",
        "age": 31,
        "experience": [
            {
                "title": "Full Stack Developer",
                "location": "Peru",
                "start_date": "2018"
            }
        ],
        "skills": [
            {
                "name": "Docker", 
                "year": 4},
            {
                "name": "AWS", 
                "year": 3}
        ],
        "languages": [
            {
                "name": "Spanish", 
                "level": "Nativo"},
            {
                "name": "English", 
                "level": "Avanzado"}
        ]
    })
    assert response.status_code ==201

def test_update_developer():
    response = client.put('/developers/69b45bc6364e64aad5575bba', json={
        "id": 3,
        "name": "Aldair Andrade",
        "country": "Peru",
        "age": 21,
        "experience": [
            {
                "title": "Full Stack Developer",
                "location": "Peru",
                "start_date": "2018"
            }
        ],
        "skills": [
            {
                "name": "Docker", 
                "year": 4},
            {
                "name": "AWS", 
                "year": 3}
        ],
        "languages": [
            {
                "name": "Spanish", 
                "level": "Nativo"},
            {
                "name": "English", 
                "level": "Avanzado"}
        ]
    })
    assert response.status_code ==201

def test_update_developer_no_existe():
    response = client.put('/developers/69b45bc6364e64aad557aaaa', json={
        "id": 3,
        "name": "Mondonguito Plato",
        "country": "Peru",
        "age": 21,
        "experience": [
            {
                "title": "Full Stack Developer",
                "location": "Peru",
                "start_date": "2018"
            }
        ],
        "skills": [
            {
                "name": "Docker", 
                "year": 4},
            {
                "name": "AWS", 
                "year": 3}
        ],
        "languages": [
            {
                "name": "Spanish", 
                "level": "Nativo"},
            {
                "name": "English", 
                "level": "Avanzado"}
        ]
    })
    assert response.status_code ==400

def test_delete_developer():
    response = client.delete('/developers/69b442d2646ff9516b3d9e21')
    assert response.status_code ==400
