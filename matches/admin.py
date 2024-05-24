from django.contrib import admin
from .models import Match

# Register your models here.
class MatchAdmin(admin.ModelAdmin):
    list_display = ('inviter_clan', 'invitee_clan','is_accepted')
admin.site.register(Match, MatchAdmin)