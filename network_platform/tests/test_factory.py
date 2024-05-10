import pytest

from rest_framework.test import APIClient


client = APIClient()


class TestElectroFactory:
    @pytest.mark.django_db
    def test_create_factory(
            self,
            contact,
            product,
            get_bearer_token
    ):

        url = "/main/factory/create/"

        data = {
            'name': 'test',
            'contact': contact,
            'product': product
        }

        response = client.post(
            url, data=data,
            HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}')

        assert response.status_code == 201

    @pytest.mark.django_db
    def test_create_factory_fail(
            self,
            contact,
            product,
            get_bearer_token
    ):
        url = "/main/factory/create/"

        data = {
            'name': 'test',
            'product': product
        }

        response = client.post(
            url, data=data,
            HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}')

        assert response.status_code == 400

    @pytest.mark.django_db
    def test_update_factory(
            self,
            contact,
            product,
            factory
    ):
        url = f"/main/factory/update/{factory}/"

        data = {
            'name': 'Test1'
        }

        response = client.patch(
            url, data=data)

        assert response.status_code == 401

    @pytest.mark.django_db
    def test_get_list_factory(
            self,
            get_bearer_token
    ):
        url = "/main/factory/list/?country=test"

        response = client.get(
            url,
            HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}')

        assert response.status_code == 200

    @pytest.mark.django_db
    def test_retrieve_factory(
            self,
            factory,
            get_bearer_token
    ):
        url = f"/main/factory/{factory}/"

        response = client.get(
            url,
            HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}')

        assert response.status_code == 200

    @pytest.mark.django_db
    def test_delete_factory(
            self,
            factory,
            get_bearer_token
    ):
        url = f"/main/factory/delete/{factory}/"

        response = client.delete(
            url,
            HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}')

        assert response.status_code == 204
