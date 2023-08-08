from django.test import TestCase

from organisation.models import Organisation
from intent.models import Intent
from rest_framework.test import APITestCase
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_200_OK
from product.models import Products


class IntentModelTestCase(TestCase):
    def setUp(self):
        # Create test data for Intent model
        self.organisation_data = {
            'name': 'Test Organisation',
            'client_id': 'test_client',
            'api_key': 'test_api_key'
        }
        self.organisation = Organisation.objects.create(**self.organisation_data)

        self.product_data = {
            'name': 'Test Product',
            'organisation': self.organisation
        }
        self.product = Products.objects.create(**self.product_data)

        self.intent_data = {
            'products': self.product,
            'name': 'Test Intent',
            'organisation': self.organisation
        }

    def test_intent_creation(self):
        intent = Intent.objects.create(**self.intent_data)
        self.assertEqual(intent.name, 'Test Intent')
        self.assertEqual(intent.organisation, self.organisation)
        self.assertEqual(intent.products, self.product)


class IntentAPITestCase(APITestCase):
    def setUp(self):
        self.organisation = Organisation.objects.create(name='Test Organisation',
                                                        client_id='test_client', api_key='test_api_key')
        self.product = Products.objects.create(name='Test Product', organisation=self.organisation)

    def test_create_valid_data(self):
        url = '/intents/'
        data = {
            'name': 'Test Intent',
            'products': str(self.product.id),
            'organisation': str(self.organisation.id)
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(Intent.objects.count(), 1)

    def test_update_valid_data(self):
        self.intent = Intent.objects.create(products=self.product, name='Test Intent',
                                            organisation=self.organisation)
        url = f'/intents/{self.intent.id}/'
        data = {'products': self.product.id, 'name': 'Updated Intent', 'organisation': self.organisation.id}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, HTTP_200_OK)
        updated_intent = Intent.objects.get(id=self.intent.id)
        self.assertEqual(updated_intent.name, 'Updated Intent')

    def test_delete(self):
        self.intent = Intent.objects.create(products=self.product, name='Test Intent',
                                            organisation=self.organisation)
        url = f'/intents/{self.intent.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
        self.assertFalse(Intent.objects.filter(id=self.intent.id).exists())

    def test_put_invalid_data(self):
        self.intent = Intent.objects.create(products=self.product, name='Test Intent',
                                            organisation=self.organisation)
        url = f'/intents/{self.intent.id}/'
        data = {'products': self.product.id, 'name': '',
                'organisation': self.organisation.id}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.intent.refresh_from_db()  # Make sure the data didn't change
        self.assertNotEqual(self.intent.name, '')

    def test_create_invalid_data(self):
        url = f'/intents/'
        data = {'products': self.product.id, 'name': '',
                'organisation': self.organisation.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(Intent.objects.count(), 0)
