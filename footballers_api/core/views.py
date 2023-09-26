from rest_framework.viewsets import ModelViewSet
import django_filters.rest_framework
from rest_framework.pagination import LimitOffsetPagination


class BaseModelViewSet(ModelViewSet):
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # filterset_fields = '__all__'
    pagination_class = LimitOffsetPagination