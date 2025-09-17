from app import app

def test_index():
    client = app.test_client()
    resp = client.get('/')
    assert resp.status_code == 200
    assert b'Hello' in resp.data

def test_predict():
    client = app.test_client()
    resp = client.post('/predict', json={"x": [1,2,3]})
    assert resp.status_code == 200
    data = resp.get_json()
    assert "prediction" in data
