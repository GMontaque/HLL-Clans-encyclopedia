from django.contrib import admin
from .models import Clan

# Register your models here.
from django.contrib import admin
from .models import Clan

class ClanAdmin(admin.ModelAdmin):
    list_display = ('clan_name', 'user')

admin.site.register(Clan, ClanAdmin)