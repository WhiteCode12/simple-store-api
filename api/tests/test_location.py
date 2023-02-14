"""
Tests for location API.
"""
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from api import models

from api.serializers import LocationSerializer


LOCATIONS_GET_URL = reverse('api:locations')
LOCATION_POST_URL = reverse('api:creare-location')


def singleLocation_url(location_id):
    """Create and return a single location URL."""
    return reverse('api:single-location', args=[location_id])


def deletelocation_url(location_id):
    """Return the delete location URL."""
    return reverse('api:delete-location', args=[location_id])


def create_location(name='TestLocation'):
    return models.Location.objects.create(name=name)


class PublicLocationAPITests(TestCase):
    """Test unauthenticat API request."""

    def setUp(self):
        self.client = APIClient()

    def test_recive_locations(self):
        """Test retrievinng a list of locations."""
        create_location()
        create_location(name='TestLocation2')

        res = self.client.get(LOCATIONS_GET_URL)

        locations = models.Location.objects.all().order_by('-id')
        serializer = LocationSerializer(locations, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_get_single_location(self):
        """Test retrievinng a single locoation."""
        location = create_location()

        url = singleLocation_url(location.id)
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        serializer = LocationSerializer(location, many=False)

        self.assertEqual(res.data, serializer.data)

    def test_create_location(self):
        """Test creating a new location."""
        payload = {
            'name': 'Suceava',
        }

        res = self.client.post(LOCATION_POST_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        location = models.Location.objects.get(id=res.data['id'])
        self.assertEqual(location.name, payload['name'])

    def test_delete_location(self):
        """Test deleting a location."""
        location = create_location()

        url = deletelocation_url(location.id)
        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertFalse(models.Location.objects.filter(id=location.id).exists())



