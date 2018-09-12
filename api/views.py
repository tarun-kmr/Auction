from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import AuctionItem, Bid
from .serializers import AuctionSerializer, BidSerializer


class AuctionItemView(viewsets.ModelViewSet):
    queryset = AuctionItem.objects.all()
    serializer_class = AuctionSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BidView(viewsets.ModelViewSet):
    queryset = Bid.objects.all()
    serializer_class = BidSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, *args, **kwargs):
        if self.request.user.is_anonymous:
            return None
        return Bid.objects.all().filter(user=self.request.user)

