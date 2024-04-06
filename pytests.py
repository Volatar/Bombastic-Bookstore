import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Bombastic Bookstore" in response.data


def test_login(client):
    response = client.post('/login', data=dict(
        username='test',
        password='test'
    ), follow_redirects=True)
    assert response.status_code == 200
    assert b"Invalid input" in response.data


def test_registration(client):
    response = client.post('/register', data=dict(
        username='test',
        email='test@example.com',
        password='test',
        confirm_password='test'
    ), follow_redirects=True)
    assert response.status_code == 200
    assert b"registered" in response.data


def test_logout(client):
    response = client.get('/logout', follow_redirects=True)
    assert response.status_code == 200
    assert b"Welcome to Bombastic Login" in response.data


def test_display_catalog(client):
    response = client.get('/catalog')
    assert response.status_code == 200
    assert b"Catalog Page" in response.data


def test_search(client):
    response = client.get('/search?query=test&search_type=title')
    assert response.status_code == 200
    assert b"Search Results" in response.data

def test_display_page(client):
    response = client.get('/display/1')
    assert response.status_code == 200
    assert b"Books Displayed" in response.data


def test_add_to_cart(client):
    response = client.post('/add_to_cart', data=dict(
        title='Book Title'
    ), follow_redirects=True)
    assert response.status_code == 200
    assert b"Book added to cart" in response.data


def test_remove_from_cart(client):
    response = client.post('/remove_from_cart', data=dict(
        title='Book Title'
    ), follow_redirects=True)
    assert response.status_code == 200
    assert b"Book removed from cart" in response.data


def test_cart(client):
    response = client.get('/cart')
    assert response.status_code == 200
    assert b"Your Cart" in response.data


def test_checkout(client):
    response = client.get('/checkout')
    assert response.status_code == 200
    assert b"Checkout" in response.data


def test_process_payment(client):
    response = client.post('/process_payment', data=dict(
        card_number_last4='3456',
        card_holder_name='Test User'
    ))
    assert response.status_code == 200
    assert b"Payment processed successfully" in response.data


def test_receipt(client):
    response = client.post('/receipt', data=dict(
        book_titles_with_quantity='Book Title x2',
        total_of_all_books='50.00',
        card_holder_name='Test User',
        street='123 Test St',
        city='Test City',
        state='Test State',
        postal_code='12345'
    ))
    assert response.status_code == 200
    assert b"Receipt" in response.data

