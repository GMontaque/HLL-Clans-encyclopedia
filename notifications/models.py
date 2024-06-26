from django.db import models
from django.contrib.auth.models import User
from clan_pages.models import Clan
from matches.models import Match

# creates notification database
class Notification(models.Model):
    issuer = models.ForeignKey(User, verbose_name=("Issuer"),
                               on_delete=models.CASCADE,
                               related_name='issuer')
    receiver = models.ForeignKey(User, verbose_name=("Receiver"),
                                 on_delete=models.CASCADE,
                                 related_name='receiver')
    clan = models.ForeignKey(Clan, verbose_name=("Clan"),
                             on_delete=models.CASCADE, null=True, blank=True)  # Allow null and blank values
    content = models.TextField(verbose_name=("Content"), max_length=100)
    status = models.CharField(max_length=50, choices=[
        ("completed", "completed"),
        ("in-progress", "in-progress"),
        ("rejected", "rejected"),
    ], default='in-progress')
    create_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True, auto_now_add=False)