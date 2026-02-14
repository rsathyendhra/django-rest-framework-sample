from rest_framework import  viewsets
from biscuits.models import BiscuitStock
from biscuits.serializers import BiscuitStockSerializer


# Create your views here.
class BiscuitsViewSet(viewsets.ModelViewSet):
    queryset = BiscuitStock.objects.all().order_by("name")
    serializer_class = BiscuitStockSerializer
