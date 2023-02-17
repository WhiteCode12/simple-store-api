"""
Tests for items API.
"""
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from api.models import Item, Location

from api.serializers import ItemSerializer


ITEMS_URL = reverse('api:items')


def create_location(name='Test Location'):
    """Create and return a sample location."""
    return Location.objects.create(name=name)


def create_item(**params):
    defaults = {
        'name': 'defaultName',
        'itemLocation': create_location(),
    }
    defaults.update(params)
    item = Item.objects.create(**defaults)
    return item


class PublicItemAPITests(TestCase):
    """Test unauthenticated API requests."""

    def setUp(self):
        self.client = APIClient()

    def test_receive_items(self):
        """Test receiving a list of items."""
        create_item()
        create_item()

        res = self.client.get(ITEMS_URL)

        items = Item.objects.all().order_by('-id')
        serializer = ItemSerializer(items, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data,serializer.data)
