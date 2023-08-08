from django.test import TestCase
from .models import Organisation
from rest_framework.test import APITestCase
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_200_OK, HTTP_400_BAD_REQUEST


class OrganisationModelTestCase(TestCase):
    def setUp(self):
        self.organisation_data = {
            'name': 'Test Organisation',
            'client_id': 'test_client',
            'api_key': 'test_api_key'
        }

    def test_organisation_creation(self):
        organisation = Organisation.objects.create(**self.organisation_data)
        self.assertEqual(organisation.name, 'Test Organisation')
        self.assertEqual(organisation.client_id, 'test_client')
        self.assertEqual(organisation.api_key, 'test_api_key')


class OrganisationAPITestCase(APITestCase):

    def test_create_valid_data(self):
        url = '/organisations/'
        data = {
            'name': 'Test Organisation',
            'client_id': 'test_client',
            'api_key': 'test_api_key'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(Organisation.objects.get().name, 'Test Organisation')

    def test_update_valid_data(self):
        self.organisation = Organisation.objects.create(name='Test Organisation', client_id='test_client',
                                                        api_key='test_api_key')
        url = f'/organisations/{self.organisation.id}/'
        data = {'name': 'Updated Organisation', 'client_id': self.organisation.client_id,
                'api_key': self.organisation.api_key}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, HTTP_200_OK)
        updated_organisation = Organisation.objects.get(id=self.organisation.id)
        self.assertEqual(updated_organisation.name, 'Updated Organisation')

    def test_delete(self):
        self.organisation = Organisation.objects.create(name='Test Organisation', client_id='test_client',
                                                        api_key='test_api_key')
        url = f'/organisations/{self.organisation.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)

        self.assertFalse(Organisation.objects.filter(id=self.organisation.id).exists())

    def test_create_invalid_data(self):
        url = '/organisations/'
        data = {
            'name': '',
            'client_id': 'test_client',
            'api_key': 'test_api_key'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(Organisation.objects.count(), 0)

    def test_update_invalid_data(self):
        self.organisation = Organisation.objects.create(name='Test Organisation', client_id='test_client',
                                                        api_key='test_api_key')
        url = f'/organisations/{self.organisation.id}/'
        data = {'name': 'Updated Organisation', 'client_id': '',
                'api_key': 'Updated api key'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        updated_organisation = Organisation.objects.get(id=self.organisation.id)
        self.assertNotEqual(updated_organisation.name, 'Updated Organisation')
        self.assertNotEqual(updated_organisation.client_id, '')
