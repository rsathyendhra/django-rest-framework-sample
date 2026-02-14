from cakes.models import CakeStock
from rest_framework import serializers

class CakeStockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CakeStock
        fields = ["name","quantity","price"]
