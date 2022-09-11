from .serializers import NodeSerializer, EdgeSerializer, NodeResponseSerializer, EdgeResponseSerializer
from .models import Node, Edge
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
from django.db import transaction
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_yasg.utils import swagger_auto_schema


class NodesView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=NodeSerializer(many=True))
    @transaction.atomic
    def post(self, request):
        serializer = NodeSerializer(request.data, many=True)
        for node in serializer.data:
            node = dict(node)
            node_model = Node.objects.filter(user=request.user, custom_id=node.get('id')).first()
            if node_model:
                node_model.data = node.get('data')
            else:
                node_model = Node.objects.create(user=request.user, custom_id=node.get('id'), data=node.get('data'))
            node_model.save()
        return JsonResponse(status=200, data={"message": "Success"}, safe=False)

    @swagger_auto_schema(responses={200: NodeResponseSerializer(many=True)})
    def get(self, request):
        nodes = Node.objects.filter(user=request.user)
        serializer = NodeResponseSerializer(data=nodes, many=True)
        serializer.is_valid()
        return JsonResponse(serializer.data, status=200, safe=False)


class EdgesView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=EdgeSerializer(many=True))
    @transaction.atomic
    def post(self, request):
        serializer = EdgeSerializer(request.data, many=True)
        for edge in serializer.data:
            edge = dict(edge)
            edge_model = Edge.objects.filter(user=request.user, custom_id=edge.get('id')).first()
            if edge_model:
                edge_model.source = edge.get('source')
                edge_model.target = edge.get('target')
                edge_model.data = edge.get('data')
            else:
                edge_model = Edge.objects.create(user=request.user,
                                                 custom_id=edge.get('id'),
                                                 source=edge.get('source'),
                                                 target=edge.get('target'),
                                                 data=edge.get('data'))
            edge_model.save()
        return JsonResponse(status=200, data={"message": "Success"}, safe=False)

    @swagger_auto_schema(responses={200: EdgeResponseSerializer(many=True)})
    def get(self, request):
        edges = Edge.objects.filter(user=request.user)
        serializer = EdgeResponseSerializer(data=edges, many=True)
        serializer.is_valid()
        return JsonResponse(serializer.data, status=200, safe=False)


class EdgeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=EdgeSerializer())
    @transaction.atomic
    def post(self, request, pk):
        edge = request.data
        edge = dict(edge)
        edge_id = pk or edge.get('id')
        edge_model = Edge.objects.filter(user=request.user, custom_id=edge_id).first()
        if edge_model:
            edge_model.source = edge.get('source')
            edge_model.target = edge.get('target')
            edge_model.data = edge.get('data')
        else:
            edge_model = Edge.objects.create(user=request.user,
                                             custom_id=edge_id,
                                             source=edge.get('source'),
                                             target=edge.get('target'),
                                             data=edge.get('data'))
        edge_model.save()
        return JsonResponse(status=200, data={"message": "Success"}, safe=False)

    @swagger_auto_schema(responses={200: EdgeResponseSerializer()})
    def get(self, request, pk):
        try:
            edge = Edge.objects.get(user=request.user, custom_id=pk)
            serializer = EdgeResponseSerializer(edge)
            return JsonResponse(status=200, data={"message": "Success", "data": serializer.data}, safe=False)
        except Edge.DoesNotExist:
            return HttpResponseNotFound("Edge doesn't exist")


class NodeView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=NodeResponseSerializer(), response={200: NodeResponseSerializer})
    @transaction.atomic
    def post(self, request, pk):
        node = request.data
        node_id = pk or node.get('id')
        node_model = Node.objects.filter(user=request.user, custom_id=node_id).first()
        if node_model:
            node_model.data = node.get('data')
        else:
            node_model = Node.objects.create(user=request.user, custom_id=node_id, data=node.get('data'))
        node_model.save()
        return JsonResponse(status=200, data={"message": "Success"}, safe=False)

    @swagger_auto_schema(responses={200: NodeResponseSerializer()})
    def get(self, request, pk):
        try:
            node = Node.objects.get(user=request.user, custom_id=pk)
            serializer = NodeResponseSerializer(node)
            return JsonResponse(status=200, data={"message": "Success", "data": serializer.data}, safe=False)
        except Node.DoesNotExist:
            return HttpResponseNotFound("Edge doesn't exist")
