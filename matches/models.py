from django.db import models
from clan_pages.models import Clan

gametype = {
    "18vs18": 0,
    "50vs50": 1,
    "30vs30": 2,
    "Tank": 3,
    "Other": 4,
}


# Create your models here.
class Match(models.Model):
    """
    """
    inviter_clan = models.ForeignKey(Clan, verbose_name=(""), on_delete=models.CASCADE,related_name='inviter')
    invitee_clan = models.ForeignKey(Clan, verbose_name=(""), on_delete=models.CASCADE,related_name='invitee')
    game_type = models.IntegerField()
    match_date = models.DateTimeField()
    message = models.TextField()
    is_accepted = models.BooleanField((""))
