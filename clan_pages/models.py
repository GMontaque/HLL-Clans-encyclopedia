from django.db import models
from django.contrib.auth.models import User

# database layout for clans
class Clan(models.Model):
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    clan_name = models.CharField("Clan Name", max_length=50)
    content = models.CharField("Content", max_length=2000)
    image_url = models.CharField("Image URL", max_length=50,blank=True,null=True)
    discord_url = models.CharField("Discord URL", max_length=50)
    website_url = models.CharField("Website URL", max_length=50,blank=True,null=True)
    
    def __str__(self):
        return self.clan_name