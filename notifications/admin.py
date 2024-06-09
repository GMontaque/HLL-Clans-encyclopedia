from django.contrib import admin
from .models import Notification


# Register your models here.
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('issuer', 'receiver', 'status')


admin.site.register(Notification, NotificationAdmin)
