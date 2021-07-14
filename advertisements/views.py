from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwnerPermissionOrIsAdminUser
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['creator__id', 'status']
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""

        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsOwnerPermissionOrIsAdminUser(), IsAuthenticated()]
        return []
