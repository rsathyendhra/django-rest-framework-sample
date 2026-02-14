from django.urls import include,path
from rest_framework import routers

from biscuits.views import BiscuitsViewSet
from cakes.views import CakeStockViewset

router = routers.DefaultRouter()
router.register(r"biscuits",BiscuitsViewSet)
router.register("cakes",CakeStockViewset)

urlpatterns = [
    path("",include(router.urls))
]
