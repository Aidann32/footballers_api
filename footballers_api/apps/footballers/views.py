from rest_framework import viewsets
import django_filters.rest_framework
from rest_framework.pagination import LimitOffsetPagination

from .models import Footballer
from .serializers import FootballerSerializer


class FootballerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Footballer.objects.all()
    serializer_class = FootballerSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = '__all__'
    pagination_class = LimitOffsetPagination
