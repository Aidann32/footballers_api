from rest_framework import viewsets

from .models import Footballer
from .serializers import FootballerSerializer


class FootballerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Footballer.objects.all()
    serializer_class = FootballerSerializer
