from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    created_at = filters.DateFromToRangeFilter(field_name='created_at')

    STATUS_CHOICES = (
        ('OPEN', 'Открыто'),
        ('CLOSED', 'Закрыто'),
    )

    status = filters.ChoiceFilter(choices=STATUS_CHOICES)

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status']
