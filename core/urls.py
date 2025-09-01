from django.urls import path
from .views import (
    PropertyListCreateView,
    PropertyDetailView,
    PropertyUpdateView,
    PropertyDeleteView,
)

urlpatterns = [
    path("properties/", PropertyListCreateView.as_view(), name="property-list-create"),
    path("properties/<int:pk>/", PropertyDetailView.as_view(), name="property-detail"),
    path("properties/<int:pk>/update/", PropertyUpdateView.as_view(), name="property-update"),
    path("properties/<int:pk>/delete/", PropertyDeleteView.as_view(), name="property-delete"),
]
