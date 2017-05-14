from terms.models import Definition
from terms.serializers import DefinitionSerializer, EquationSerializer

from rest_framework import viewsets
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

import helper


class DefinitionViewSet(viewsets.ModelViewSet):
    queryset = Definition.objects.all()
    serializer_class = DefinitionSerializer

    def get_queryset(self):
        queryset = Definition.objects.all()
        requested = self.request.query_params.get('terms', None)
        if requested is not None:
            requested = requested.split(",")
            queryset = queryset.filter(name__in=requested)
        return queryset


class EquationViewSet(viewsets.ViewSet):
    queryset = Definition.objects.all()
    serializer_class = EquationSerializer

    def retrieve(self, request, pk=None):
        requested = request.query_params.get('terms', None)
        if requested is not None:
            requested = set(requested.split(","))
        equations = helper.find_complete_definitions()
        results = {}
        for eq in equations:
            if requested and eq in requested:
                results[eq] = equations[eq]
            elif requested is None:
                results[eq] = equations[eq]
        return Response(results)

    def list(self, request):
        return self.retrieve(request)
