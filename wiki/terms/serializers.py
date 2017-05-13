from terms.models import Definition

from rest_framework import serializers


class DefinitionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Definition
        fields = ('name', 'definition', 'short_definition', 'source', 'equation')
