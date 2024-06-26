from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import UserProfile

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False

class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)

    list_display = ('username', 'email', 'first_name', 'last_name',
                    'is_staff', 'is_clan_rep', 'memorable_name')

    def is_clan_rep(self, instance):
        try:
            return instance.userprofile.clan_rep
        except UserProfile.DoesNotExist:
            UserProfile.objects.create(user=instance)
            return False

    def memorable_name(self, instance):
        return instance.userprofile.memorable_name

    is_clan_rep.boolean = True
    is_clan_rep.short_description = 'Clan Representative'

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)
