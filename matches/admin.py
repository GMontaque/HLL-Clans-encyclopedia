from django.contrib import admin
from .models import Match


# displays data on admin page by inviter_clan, invitee_clan, is_accepted
class MatchAdmin(admin.ModelAdmin):
    list_display = ('inviter_clan', 'invitee_clan', 'is_accepted')


admin.site.register(Match, MatchAdmin)
