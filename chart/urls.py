from django.urls import path
from .views import NodesView, EdgesView, NodeView, EdgeView

urlpatterns = [
    path('nodes', NodesView.as_view(), name='nodes'),
    path('edges', EdgesView.as_view(), name='edges'),
    path('node/<int:pk>', NodeView.as_view(), name='node'),
    path('edge/<pk>', EdgeView.as_view(), name='edge'),
]
