from django.db import models
from django.contrib.auth.models import User
from clan_pages.models import Clan
from matches.models import Match

class Notification(models.Model):
    content = models.CharField(("Content"), max_length=50)
    issuer = models.ForeignKey(User, verbose_name=("Issuer"), on_delete=models.CASCADE,related_name='issuer')
    receiver = models.ForeignKey(User, verbose_name=("Receiver"), on_delete=models.CASCADE,related_name='receiver')
    # status = models.IntegerField((""))
    status = models.CharField(max_length=50, choices=[
        ("completed", "completed"),
        ("in-progress", "in-progress"),
        ("rejected", "rejected"),
    ])
    clan = models.ForeignKey(Clan, verbose_name=("Clan"), on_delete=models.CASCADE)
    match = models.ForeignKey(Match, verbose_name=("Match"), on_delete=models.CASCADE)
