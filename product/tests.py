from django.test import TestCase

from organisation.models import Organisation
from product.models import Products
from rest_framework.test import APITestCase
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_200_OK


class ProductModelTestCase(TestCase):
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

    def test_product_creation(self):
        intent = Products.objects.create(**self.product_data)
        self.assertEqual(intent.name, 'Test Product')
        self.assertEqual(intent.organisation, self.organisation)


class ProductAPITestCase(APITestCase):
    def setUp(self):
        self.organisation = Organisation.objects.create(name='Test Organisation',
                                                        client_id='test_client', api_key='test_api_key')

    def test_create_valid_data(self):
        url = '/products/'
        data = {
            'name': 'Test Product',
            'organisation': str(self.organisation.id)
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(Products.objects.count(), 1)
        self.assertEqual(Products.objects.get().name, 'Test Product')

    def test_update_valid_data(self):
        self.product = Products.objects.create(name='Test Intent',
                                               organisation=self.organisation)
        url = f'/products/{self.product.id}/'
        data = {'name': 'Updated Product', 'organisation': self.organisation.id}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, HTTP_200_OK)

        updated_product = Products.objects.get(id=self.product.id)
        self.assertEqual(updated_product.name, 'Updated Product')

    def test_delete(self):
        self.product = Products.objects.create(name='Test Product',
                                               organisation=self.organisation)
        url = f'/products/{self.product.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)

        self.assertFalse(Products.objects.filter(id=self.product.id).exists())

    def test_put_invalid_data(self):
        self.product = Products.objects.create(name='Test Product',
                                               organisation=self.organisation)
        url = f'/products/{self.product.id}/'
        data = {'name': '', 'organisation': self.organisation.id}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.product.refresh_from_db()  # Make sure the data didn't change
        self.assertNotEqual(self.product.name, '')

    def test_create_invalid_data(self):
        url = f'/products/'
        data = {'name': '', 'organisation': self.organisation.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(Products.objects.count(), 0)
