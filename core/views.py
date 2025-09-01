from rest_framework import generics, permissions
from rest_framework.exceptions import PermissionDenied
from .models import Property
from .serializers import PropertySerializer


class PropertyListCreateView(generics.ListCreateAPIView):
    queryset = Property.objects.all().order_by("-created_at")
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        if self.request.user.role != "owner":
            raise PermissionDenied("Only owners can create properties.")
        serializer.save(owner=self.request.user)


class PropertyDetailView(generics.RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.AllowAny]


class PropertyUpdateView(generics.UpdateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_update(self, serializer):
        property_obj = self.get_object()
        if property_obj.owner != self.request.user:
            raise PermissionDenied("You can only update your own property.")
        serializer.save()


class PropertyDeleteView(generics.DestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_destroy(self, instance):
        if instance.owner != self.request.user:
            raise PermissionDenied("You can only delete your own property.")
        instance.delete()
