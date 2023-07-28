from django.contrib import admin

# Register your models here.
from .models import Auction,Collector,ArtPiece

admin.site.register(Auction)
admin.site.register(Collector)
admin.site.register(ArtPiece)

