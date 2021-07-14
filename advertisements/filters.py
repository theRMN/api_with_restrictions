from django_filters import rest_framework as filters


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    created_at = filters.DateFromToRangeFilter(field_name='created_at')

