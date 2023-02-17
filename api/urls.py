from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('locations/', views.getLocations, name='locations'),
    path('location/<str:pk>/', views.getlocation, name='single-location'),
    path('createlocation/', views.createLocation, name='creare-location'),
    path('deletelocation/<str:pk>/', views.deleteLocation, name='delete-location'),
    path('items/', views.getItems, name='items'),
]
