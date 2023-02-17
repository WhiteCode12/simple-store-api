"""
Serializer for location and item APIs.
"""

from rest_framework import serializers

from .models import Location, Item


class LocationSerializer(serializers.ModelSerializer):
    """Serialiizer for locations."""

    class Meta:
        model = Location
        fields = '__all__'
        read_only_fields = ['id']


class ItemSerializer(serializers.ModelSerializer):
    """Serializer for items."""

    class Meta:
        model = Item
        fields = ['id', 'name', 'itemLocation']
        read_only_fields = ['id']
