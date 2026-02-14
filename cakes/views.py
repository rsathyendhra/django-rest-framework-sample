from django.shortcuts import render
from rest_framework import viewsets
from cakes.models import CakeStock
from cakes.serializers import CakeStockSerializer

# Create your views here.
class  CakeStockViewset(viewsets.ModelViewSet):
    queryset = CakeStock.objects.all().order_by("name")
    serializer_class = CakeStockSerializer
