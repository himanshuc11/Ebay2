from django.db import models
from customUser.models import User

# Create your models here.
ITEM_CATEGORY_CHOICES = [
    ('ELECTRONICS', 'ELECTRONICS'),
    ('FASHION', 'FASHION'),
    ('MISC', 'MISC')
]
class Category(models.Model):
    item_category = models.CharField(max_length=128, choices=ITEM_CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.item_category}"

class Items(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512)
    owner = models.ForeignKey(User, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Category)
    image = models.ImageField(null=True,blank=True,upload_to='image/')

    def __str__(self):
        return f"{self.name}"

class Comment(models.Model):
    comment = models.TextField()
    product = models.ForeignKey(Items, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}: commented {self.comment} on : {self.product}"

class Bid(models.Model):
    amount = models.PositiveIntegerField()
    bidder = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Items, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.bidder} bids {self.amount} on {self.product}"