import pytest

from rest_framework.test import APIClient

client = APIClient()


@pytest.fixture
def test_user_create():
    return '/user/create/'


@pytest.fixture
def test_user_list():
    return '/user/list/'


@pytest.fixture
def test_user_retrieve():
    return '/user/'


@pytest.fixture
def test_user_update():
    return '/user/update/'


@pytest.fixture
def test_user_destroy():
    return '/user/delete/'


@pytest.fixture
def test_get_token():
    return '/api/token/'


@pytest.fixture
def get_bearer_token(test_user_create, test_get_token):
    create_url = test_user_create
    token_url = test_get_token

    create_data = {
        'email': 'test@example.com',
        'password': 'test123456',
        'name': 'Test Name',
        'surname': 'Test Surname',
        'is_staff': True,
        'is_superuser': True,
        'is_active': True,
    }

    token_data = {
        'email': 'test@example.com',
        'password': 'test123456',
    }

    client.post(create_url, create_data)
    get_user_token = client.post(token_url, token_data)

    return get_user_token.data['access']
