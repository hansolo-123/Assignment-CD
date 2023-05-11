from main import app

# Test that the index route returns a 200 status code
def test_index_route():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

# Test that the index route returns the expected response
def test_index_response():
    client = app.test_client()
    response = client.get('/')
    assert response.get_data(as_text=True) == 'Hello, world!'

# Test that the cow route returns the expected response
def test_cow_response():
    client = app.test_client()
    response = client.get('/cow')
    assert response.get_data(as_text=True) == 'MOoooOo!'
