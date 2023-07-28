from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


# Collector (customer) - replaces django user model.
class MyUser(AbstractUser):
    address = models.CharField(max_length=100, null=False)
    
    def __str__(self):
        return self.username

# ArtPiece (product)
class ArtPiece(models.Model):
    name = models.CharField(max_length=100, null=False)
    # one collector for this artpice. Foreign key .
    collector = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.name} - {self.id}"
    
# Auction
class Auction(models.Model):
    name = models.CharField(max_length=100, null=False)
    art_piece = models.ManyToManyField(ArtPiece)

    def __str__(self):
        return self.name
