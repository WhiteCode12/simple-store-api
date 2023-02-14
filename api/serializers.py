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
