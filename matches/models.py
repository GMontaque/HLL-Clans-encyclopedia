from django.db import models
from clan_pages.models import Clan

# Create your models here.
class Match(models.Model):
    """
    """
    inviter_clan = models.ForeignKey(Clan, verbose_name=("Inviter"), on_delete=models.CASCADE,related_name='inviter')
    invitee_clan = models.ForeignKey(Clan, verbose_name=("Invitee"), on_delete=models.CASCADE,related_name='invitee')
    # game_type = models.IntegerField()
    game_type = models.CharField(max_length=10, choices=[
        ("", "Select from the list below"),
        ("18vs18", "18vs18"),
        ("50vs50", "50vs50"),
        ("30vs30", "30vs30"),
        ("Tank", "Tank"),
        ("Other", "Other"),
    ])
    match_date = models.DateTimeField()
    message = models.TextField()
    is_accepted = models.BooleanField(("Is Accepted"))
