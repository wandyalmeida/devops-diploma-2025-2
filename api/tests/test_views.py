from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

class BookViewTest(APITestCase):
    def test_response_is_correct(self):
        #
        # 200 =< 300 sucessful
        # 400 =< 500 bad request 
        # 500 so bad request 
        url = reverse('api:books')
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        body = response.json()
        assert body['hello'] == 'django'

class HealthViewTest(APITestCase):

    def test_response_is_correct(self):
        #
        # 200 =< 300 sucessful
        # 400 =< 500 bad request 
        # 500 so bad request 
        url = reverse('api:health')
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        body = response.json()
        assert body['status'] == 'OK'
