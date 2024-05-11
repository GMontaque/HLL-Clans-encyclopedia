from django.db import models
from django.contrib.auth.models import User
from clan_pages.models import Clan
from matches.models import Match

# Create your models here.
status = {
    "completed": 0,
    "in-progress": 1,
    "rejected ": 2,
}

class Notification(models.Model):
    content = models.CharField((""), max_length=50)
    issuer = models.ForeignKey(User, verbose_name=(""), on_delete=models.CASCADE,related_name='issuer')
    receiver = models.ForeignKey(User, verbose_name=(""), on_delete=models.CASCADE,related_name='receiver')
    status = models.IntegerField((""))
    clan = models.ForeignKey(Clan, verbose_name=(""), on_delete=models.CASCADE)
    match = models.ForeignKey(Match, verbose_name=(""), on_delete=models.CASCADE)
