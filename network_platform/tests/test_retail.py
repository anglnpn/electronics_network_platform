import pytest

from rest_framework.test import APIClient

client = APIClient()


class TestRetail:
    @pytest.mark.django_db
    def test_create_retail(
            self,
            contact,
            product,
            factory,
            get_bearer_token
    ):
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

        assert response.status_code == 201

    @pytest.mark.django_db
    def test_create_retail_fail(
            self,
            contact,
            product,
            get_bearer_token
    ):
        url = "/main/retail/create/"

        data = {
            'name': 'test',
            'product': product
        }

        response = client.post(
            url, data=data,
            HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}')

        assert response.status_code == 400

    @pytest.mark.django_db
    def test_update_retail(
            self,
            retail,
            get_bearer_token
    ):
        url = f"/main/retail/update/{retail}/"

        data = {
            'name': 'Test1'
        }

        response = client.patch(
            url, data=data,
            HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}'
        )

        assert response.status_code == 200

    @pytest.mark.django_db
    def test_update_retail_fail(
            self,
            retail,
            get_bearer_token
    ):
        url = f"/main/retail/update/{retail}/"

        data = {
            'debt': 2000.00
        }

        response = client.patch(
            url, data=data,
            HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}'
        )

        assert response.status_code == 400

    @pytest.mark.django_db
    def test_get_list_retail(
            self,
            get_bearer_token
    ):
        url = "/main/retail/list/?country=test"

        response = client.get(
            url,
            HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}')

        assert response.status_code == 200

    @pytest.mark.django_db
    def test_retrieve_factory(
            self,
            retail,
            get_bearer_token
    ):
        url = f"/main/retail/{retail}/"

        response = client.get(
            url,
            HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}')

        assert response.status_code == 200

    @pytest.mark.django_db
    def test_delete_retail(
            self,
            retail,
            get_bearer_token
    ):
        url = f"/main/retail/delete/{retail}/"

        response = client.delete(
            url,
            HTTP_AUTHORIZATION=f'Bearer {get_bearer_token}')

        assert response.status_code == 204
