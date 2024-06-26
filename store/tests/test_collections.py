import pytest
from rest_framework import status
from rest_framework.test import APIClient


class TestCreateCollection:
    @pytest.mark.skip
    def test_if_user_is_annonymous_return_401(self):
        #arrange
        #act
        client = APIClient()
        print("Client is here:", client)
        response = client.post('/store/collections/', {'title':'a'})
        print("Here",response.status_code)
        #assert
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
    @pytest.mark.django_db
    def test_if_user_is_not_admin_return_403(self):
        #arrange
        #act
        client = APIClient()
        client.force_authenticate(user={})
        print("Client is here:", client)
        response = client.post('/store/collections/', {'title':'a'})
        print("Here", response.status_code)
        #assert
        assert response.status_code == status.HTTP_403_FORBIDDEN
        