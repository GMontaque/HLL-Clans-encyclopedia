from django.contrib import admin
from .models import Clan

# Register your models here.
# displays clans on admin panel by clan name and user name who created them
class ClanAdmin(admin.ModelAdmin):
    list_display = ('clan_name', 'user')

admin.site.register(Clan, ClanAdmin)