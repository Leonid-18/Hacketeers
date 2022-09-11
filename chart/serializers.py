from rest_framework import serializers
from .models import Node, Edge
from rest_framework.serializers import ModelSerializer


class EdgeSerializer(ModelSerializer):
    class Meta:
        model = Edge
        fields = (
            'id', 'target', 'source', 'data'
        )


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ['id', 'data']
