from django.contrib import admin

# Register your models here.
from .models import Auction,MyUser,ArtPiece

admin.site.register(Auction)
admin.site.register(MyUser)
admin.site.register(ArtPiece)

