"""
Tests for models.
"""
from django.test import TestCase

from api import models


class ModelTests(TestCase):
    """Test model."""

    def test_create_location(self):
        """Test creating a location is successful."""
        location = models.Location.objects.create(
            name ='TestLocation',
        )

        self.assertEqual(str(location), location.name)
    
    def test_create_item(self):
        """Test creating a item is successful."""
        location = models.Location.objects.create(
            name='TestLocation',
        )
        item = models.Item.objects.create(
            itemLocation=location,
            name='TestItem',
        )

        self.assertEqual(str(item), item.name)
