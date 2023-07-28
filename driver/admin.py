from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Driver, Race, Team

admin.site.register(Driver)
admin.site.register(Race)
admin.site.register(Team)


