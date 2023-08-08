from django.test import TestCase

from action.models import Action
from organisation.models import Organisation
from suggestion.models import Suggestions
from rest_framework.test import APITestCase
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST, HTTP_200_OK

from suggestion.serializers import SuggestionsSerializer


class SuggestionsModelTestCase(TestCase):
    def setUp(self):
        # Create test data for Intent model
        self.organisation_data = {
            'name': 'Test Organisation',
            'client_id': 'test_client',
            'api_key': 'test_api_key'
        }
        self.organisation = Organisation.objects.create(**self.organisation_data)

        self.action_data = {
            'name': 'Test Action',
        }
        self.action = Action.objects.create(**self.action_data)

        self.suggestion_data = {
            'name': 'Test Suggestion',
            'content': {'language': 'eng', 'content_data': 'dummy data'},
            'organisation': str(self.organisation.id),
            'action': str(self.action.id)
        }

    def test_suggestion_creation(self):
        suggestion = Suggestions.objects.create(name='Test Suggestion',
                                                content={'language': 'eng', 'content_data': 'dummy data'},
                                                organisation=self.organisation,
                                                action=self.action)
        self.assertEqual(suggestion.name, 'Test Suggestion')
        self.assertEqual(suggestion.content, self.suggestion_data.get('content'))


class SuggestionsAPITestCase(APITestCase):
    def setUp(self):
        self.organisation = Organisation.objects.create(name='Test Organisation',
                                                        client_id='test_client', api_key='test_api_key')
        self.action = Action.objects.create(name='Test Action')

        self.suggestion_data = {
            'name': 'Test Suggestion',
            'content': {'language': 'eng', 'content_data': 'dummy data'},
            'organisation': str(self.organisation.id),
            'action': str(self.action.id)
        }

    def test_create_valid_data(self):
        url = '/suggestions/'
        response = self.client.post(url, self.suggestion_data, format='json')
        self.assertEqual(response.status_code, HTTP_201_CREATED)
        self.assertEqual(Suggestions.objects.count(), 1)
        self.assertEqual(Suggestions.objects.get().name, 'Test Suggestion')

    def test_update_valid_data(self):
        self.suggestion = Suggestions.objects.create(name='Test Suggestion',
                                                     content={'language': 'eng', 'content_data': 'dummy data'},
                                                     organisation=self.organisation,
                                                     action=self.action)
        url = f'/suggestions/{self.suggestion.id}/'
        data = {
            'name': 'Updated Suggestion',
            'content': {'language': 'eng', 'content_data': 'dummy data'},
            'organisation': str(self.organisation.id),
            'action': str(self.action.id)}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, HTTP_200_OK)
        updated_suggestion = Suggestions.objects.get(id=self.suggestion.id)
        self.assertEqual(updated_suggestion.name, 'Updated Suggestion')

    def test_delete(self):
        self.suggestion = Suggestions.objects.create(name='Test Suggestion',
                                                     content={'language': 'eng', 'content_data': 'dummy data'},
                                                     organisation=self.organisation,
                                                     action=self.action)
        url = f'/suggestions/{self.suggestion.id}/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)
        self.assertFalse(Suggestions.objects.filter(id=self.suggestion.id).exists())

    def test_put_invalid_data(self):
        self.suggestion = Suggestions.objects.create(name='Test Suggestion',
                                                     content={'language': 'eng', 'content_data': 'dummy data'},
                                                     organisation=self.organisation,
                                                     action=self.action)
        url = f'/suggestions/{self.suggestion.id}/'
        data = {
            'name': '',
            'content': {'language': 'eng', 'content_data': 'dummy data'},
            'organisation': str(self.organisation.id),
            'action': str(self.action.id)}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.suggestion.refresh_from_db()  # Make sure the data didn'tchange
        self.assertNotEqual(self.suggestion.name, '')

    def test_create_invalid_name(self):
        url = f'/suggestions/'
        data = {
            'name': '',
            'content': {'language': 'eng', 'content_data': 'dummy data'},
            'organisation': str(self.organisation.id),
            'action': str(self.action.id)}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)
        self.assertEqual(Suggestions.objects.count(), 0)

    def test_create_invalid_content(self):
        data = {
            'name': 'Test Suggestion',
            'content': {'content_data': 'dummy data'},
            'organisation': str(self.organisation.id),
            'action': str(self.action.id)}
        serializer = SuggestionsSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('content', serializer.errors)
