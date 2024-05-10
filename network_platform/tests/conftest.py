import pytest

from rest_framework.test import APIClient

client = APIClient()


@pytest.fixture
def get_bearer_token():
    create_url = '/user/create/'
    token_url = '/api/token/'

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
    print(get_user_token.data['access'])

    return get_user_token.data['access']


@pytest.fixture
def contact(get_bearer_token):
    url = '/main/contact/create/'

    data = {
        'email': 'test@test',
        'country': 'test',
        'city': 'test',
        'street': 'test',
        'number_home': 1
    }

    response = client.post(
        url, data=data,
        HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}')

    return response.json()["id"]


@pytest.fixture
def product(get_bearer_token):
    url = '/main/product/create/'

    data = {
        'name': 'test',
        'product_model': 'test',
    }

    response = client.post(
        url, data=data,
        HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}')
    return response.json()["id"]


@pytest.fixture
def factory(contact, product, get_bearer_token):
    url = "/main/factory/create/"

    data = {
        'name': 'test',
        'contact': contact,
        'product': product
    }

    response = client.post(
        url, data=data,
        HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}')

    return response.json()["id"]


@pytest.fixture
def retail(contact, product,
           factory, get_bearer_token):
    url = "/main/retail/create/"

    data = {
        'name': 'test',
        'contact': contact,
        'product': product,
        'provider_factory': factory,
        'debt': 10000.00
    }

    response = client.post(
        url, data=data,
        HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}')

    return response.json()["id"]


@pytest.fixture
def trader(
        contact, product,
        factory, get_bearer_token
):
    url = "/main/trader/create/"

    data = {
        'name': 'test',
        'contact': contact,
        'product': product,
        'provider_factory': factory,
        'debt': 10000.00
    }

    response = client.post(
        url, data=data,
        HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}')

    return response.json()["id"]
