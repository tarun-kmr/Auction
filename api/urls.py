from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('items', views.AuctionItemView)
router.register('bids', views.BidView)


urlpatterns = [
    path('', include(router.urls))
]

