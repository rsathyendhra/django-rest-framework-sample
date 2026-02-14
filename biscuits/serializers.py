from biscuits.models import BiscuitStock
from rest_framework import serializers

class BiscuitStockSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BiscuitStock
        fields = ["name","price","quantity"]
