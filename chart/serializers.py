from rest_framework import serializers
from .models import Node, Edge
from rest_framework.serializers import ModelSerializer


class EdgeSerializer(serializers.Serializer):
    id = serializers.CharField()
    target = serializers.CharField(required=False)
    source = serializers.CharField(required=False)
    data = serializers.CharField(max_length=100000, required=False)


class NodeSerializer(serializers.Serializer):
    id = serializers.CharField()
    data = serializers.CharField(max_length=100000, required=False)


class NodeResponseSerializer(serializers.Serializer):
    id = serializers.SerializerMethodField()
    data = serializers.CharField(max_length=100000)

    def get_id(self, obj):
        return obj.custom_id


class EdgeResponseSerializer(serializers.Serializer):
    id = serializers.SerializerMethodField()
    target = serializers.CharField()
    source = serializers.CharField()
    data = serializers.CharField(max_length=100000)

    def get_id(self, obj):
        return obj.custom_id