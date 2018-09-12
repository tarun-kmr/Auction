from datetime import date, datetime
from django.core import serializers as serialize_data
from rest_framework import serializers
from .models import AuctionItem, Bid
from django.contrib.auth.models import User


class BidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bid
        fields = ('user', 'item', 'amount_by_user')

class AuctionSerializer(serializers.HyperlinkedModelSerializer):
    bid = BidSerializer(required=False)
    class Meta:
        model = AuctionItem
        fields = (
            'url',
            'id', 'name', 'description', 'start_amount',
            'image', 'start_time', 'end_time', 'bid',
        )

    def to_representation(self, instance):
        res = super().to_representation(instance)

        today = date.today()
        query_set = list(instance.bid_set.get_queryset())
        end_time = datetime.strptime(res['end_time'], "%Y-%m-%d").date()
        highest_bids = [bid.amount_by_user for bid in query_set]
        if query_set:
            if end_time < today:
                for bid in query_set:
                    if highest_bids and bid.amount_by_user > max(highest_bids):
                        continue
                    else:
                        res['winner'] = {}
                        res['winner']['name'] = bid.user.username
                        res['winner']['amount'] = bid.amount_by_user
                        instance.winner = bid.user
                        instance.save()

            else:
                res['highest_bid_amount'] = max(highest_bids)

        return res
