import pytest

from rest_framework.test import APIClient

from users.models import User

client = APIClient()


class TestUser:
    @pytest.mark.django_db
    def test_query_create_user(
            self, test_user_create):
        url = test_user_create
        data = {
            'email': 'test@example.com',
            'password': 'test123456',
            'name': 'Test Name',
            'surname': 'Test Surname',
            'is_staff': True,
            'is_superuser': True,
        }

        response = client.post(url, data)

        query_from_db = User.objects.get()

        assert response.status_code == 201

        assert data['name'] == query_from_db.name
        assert data['surname'] == query_from_db.surname
        assert data['email'] == query_from_db.email

    @pytest.mark.django_db
    def test_bad_request_email(
            self, test_user_create):
        url = test_user_create
        data = {
            'password': 'test123456',
            'name': 'Test Name',
            'surname': 'Test Surname',
            'is_staff': True,
            'is_superuser': True,
        }

        response = client.post(url, data)

        assert response.status_code == 400
        assert response.json() == {
            'email': ['This field is required.']}

    @pytest.mark.django_db
    def test_bad_request_password(
            self, test_user_create):
        url = test_user_create
        data = {
            'email': 'test@example.com',
            'name': 'Test Name',
            'surname': 'Test Surname',
            'is_staff': True,
            'is_superuser': True,
        }

        response = client.post(url, data)

        assert response.status_code == 400
        assert response.json() == {
            'password': ['This field is required.']}

    @pytest.mark.django_db
    def test_bad_request_name(
            self, test_user_create):

        url = test_user_create
        data = {
            'email': 'test@example.com',
            'password': 'test123456',
            'surname': 'Test Surname',
            'is_staff': True,
            'is_superuser': True,
        }

        response = client.post(url, data)

        assert response.status_code == 400
        assert response.json() == {
            'name': ['This field is required.']}

    @pytest.mark.django_db
    def test_bad_request_surname(
            self, test_user_create):
        url = test_user_create
        data = {
            'email': 'test@example.com',
            'password': 'test123456',
            'name': 'Test Name',
            'is_staff': True,
            'is_superuser': True,
        }

        response = client.post(url, data)

        assert response.status_code == 400
        assert response.json() == {
            'surname': ['This field is required.']}

    @pytest.mark.django_db
    def test_query_list(self, get_bearer_token, test_user_list):
        list_url = test_user_list

        list_response = client.get(
            list_url,
            HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}')

        assert list_response.status_code == 200

    @pytest.mark.django_db
    def test_query_retrieve(
            self, get_bearer_token, test_user_retrieve):
        user_id = User.objects.get().id
        user_id_str = str(user_id)

        retrieve_url = f'/user/{user_id_str}/'

        list_response = client.get(
            retrieve_url,
            HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}')

        assert list_response.status_code == 200

    @pytest.mark.django_db
    def test_query_update(
            self, get_bearer_token, test_user_update):
        user_id = User.objects.get().id
        user_id_str = str(user_id)

        data = {
            'email': 'test@example.ru',
            'password': 'test123456',
            'name': 'Test Update',
            'is_staff': True,
            'is_superuser': True,
        }

        update_url = test_user_update + user_id_str + '/'

        list_response = client.patch(
            update_url, data,
            HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}')

        assert list_response.status_code == 200

    @pytest.mark.django_db
    def test_query_delete(
            self, get_bearer_token, test_user_destroy):
        user_id = User.objects.get().id
        user_id_str = str(user_id)

        delete_url = test_user_destroy + user_id_str + '/'

        list_response = client.delete(
            delete_url,
            HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}')

        assert list_response.status_code == 204
