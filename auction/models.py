from django.db import models
from django.contrib.auth.models import User
# from django.contrib.auth.models import AbstractUser

# class MyUser(AbstractUser):
#     pass

# Collector (customer)
class Collector(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=2)
    name = models.CharField(max_length=100, null=False)
    def __str__(self):
        return self.name

# ArtPiece (product)
class ArtPiece(models.Model):
    name = models.CharField(max_length=100, null=False)
    # one collector for this artpice. Foreign key .
    collector = models.ForeignKey(Collector, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.name} - {self.id}"
    
# Auction
class Auction(models.Model):
    name = models.CharField(max_length=100, null=False)
    art_piece = models.ManyToManyField(ArtPiece)

    def __str__(self):
        return self.name
