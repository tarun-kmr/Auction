from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class AuctionItem(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    start_amount = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to = 'pic_folder/', default = None)
    start_time = models.DateField(default=timezone.now)
    end_time = models.DateField(default=timezone.now)
    winner =  models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True
    )


class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(AuctionItem, on_delete=models.CASCADE)
    amount_by_user = models.IntegerField(blank=True, null=True)
