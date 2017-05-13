from terms.models import Definition
from terms.serializers import DefinitionSerializer

from rest_framework import viewsets


class DefinitionViewSet(viewsets.ModelViewSet):
    queryset = Definition.objects.all()
    serializer_class = DefinitionSerializer
