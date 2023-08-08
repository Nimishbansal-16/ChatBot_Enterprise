from django.test import TestCase

from intent.models import Intent
from organisation.models import Organisation
from product.models import Products
from subintent.models import SubIntent
from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_204_NO_CONTENT, HTTP_201_CREATED


class SubIntentModelTestCase(TestCase):
    def setUp(self):
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
        self.intent = Intent.objects.create(**self.intent_data)

        self.subintent_data = {
            'name': 'Test SubIntent',
            'products': self.product,
            'intent': self.intent,
            'organisation': self.organisation
        }

    def test_subintent_creation(self):
        subintent = SubIntent.objects.create(**self.subintent_data)
        self.assertEqual(subintent.name, 'Test SubIntent')
        self.assertEqual(subintent.products, self.product)
        self.assertEqual(subintent.intent, self.intent)
        self.assertEqual(subintent.organisation, self.organisation)


class SubIntentAPITestCase(APITestCase):
    def setUp(self):
        self.organisation = Organisation.objects.create(name='Test Organisation',
                                                        client_id='test_client', api_key='test_api_key')
        self.product = Products.objects.create(name='Test Product', organisation=self.organisation)
        self.intent = Intent.objects.create(products=self.product,
                                            name='Test Intent', organisation=self.organisation)

    def test_create_valid_data(self):
        url = '/subintents/'
        data = {
            'name': 'Test SubIntent',
            'products': str(self.product.id),
            'intent': str(self.intent.id),
            'organisation': str(self.organisation.id)
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(SubIntent.objects.count(), 1)
        self.assertEqual(SubIntent.objects.get().name, 'Test SubIntent')

    def test_update_valid_data(self):
        self.subintent = SubIntent.objects.create(name='Test SubIntent', products=self.product,
                                                  intent=self.intent, organisation=self.organisation)
        url = f'/subintents/{self.subintent.id}/'
        data = {'name': 'Updated SubIntent', 'products': self.product.id,
                'intent': self.intent.id, 'organisation': self.organisation.id}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, HTTP_200_OK)
        updated_subintent = SubIntent.objects.get(id=self.subintent.id)
        self.assertEqual(updated_subintent.name, 'Updated SubIntent')

    def test_delete(self):
        self.subintent = SubIntent.objects.create(name='Test SubIntent', products=self.product,
                                                  intent=self.intent, organisation=self.organisation)
        url = f'/subintents/{self.subintent.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
        self.assertFalse(SubIntent.objects.filter(id=self.subintent.id).exists())

    def test_create_invalid_data(self):
        url = '/subintents/'
        data = {
            'name': '',
            'products': str(self.product.id),
            'intent': str(self.intent.id),
            'organisation': str(self.organisation.id)
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(SubIntent.objects.count(), 0)

    def test_update_invalid_data(self):
        self.subintent = SubIntent.objects.create(name='Test SubIntent', products=self.product,
                                                  intent=self.intent, organisation=self.organisation)
        url = f'/subintents/{self.subintent.id}/'
        data = {'name': '', 'products': self.product.id,
                'intent': self.intent.id, 'organisation': self.organisation.id}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        updated_subintent = SubIntent.objects.get(id=self.subintent.id)
        self.assertNotEqual(updated_subintent.name, '')
