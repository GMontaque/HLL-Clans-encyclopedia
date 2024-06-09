from django.db import models
from clan_pages.models import Clan


# Creates match database
class Match(models.Model):
    # who requested the game
    inviter_clan = models.ForeignKey(Clan, verbose_name=("Inviter"),
                                     on_delete=models.CASCADE,
                                     related_name='inviter')
    # who the game request was sent to
    invitee_clan = models.ForeignKey(Clan, verbose_name=("Invitee"),
                                     on_delete=models.CASCADE,
                                     related_name='invitee')
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
    is_accepted = models.CharField(max_length=50, choices=[
        ("accepted", "accepted"),
        ("in-progress", "in-progress"),
        ("rejected", "rejected"),
    ], default='in-progress')
