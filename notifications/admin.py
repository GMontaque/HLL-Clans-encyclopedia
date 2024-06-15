from django.contrib import admin
from .models import Notification


# Register your models here.
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('issuer', 'receiver', 'status','create_at','update_at')


admin.site.register(Notification, NotificationAdmin)
