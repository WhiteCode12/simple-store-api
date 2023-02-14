from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from .serializers import LocationSerializer
from .models import Location


@api_view(['GET'])
def getLocations(request):
    locations = Location.objects.all().order_by('-id')
    serializer = LocationSerializer(locations, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def getlocation(request, pk):
    location = Location.objects.get(id=pk)
    serializer = LocationSerializer(location, many=False)

    return Response(serializer.data)


@api_view(['POST'])
def createLocation(request):
    data = request.data
    name = data['name']

    location, created = Location.objects.get_or_create(name=name)
    location.save()

    serializer = LocationSerializer(location, many=False)

    return Response(serializer.data)


@api_view(['DELETE'])
def deleteLocation(request, pk):
    location = Location.objects.get(id=pk)
    location.delete()

    return Response('Location was deleted!')