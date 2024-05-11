from django.db import models
from django.contrib.auth.models import User
# TODO: import match

# Create your models here.
gametype = {
    "18vs18": 0,
    "50vs50": 1,
    "30vs30": 2,
    "Tank": 3,
    "Other": 4,
}

# User account
class User(models.Model):

    # contains username
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # checks if user is a clan rep, if they click yes the navbar will update with clan creation link
    is_representative = models.BooleanField(default=None)
    # stores clan name
    # clan_name = models.CharField((""), max_length=50,default=None)

    # get email, password and username from user 
    # username = models.models.CharField(_(""), max_length=50)
    # # stores email
    # email = models.EmailField(_(""), max_length=254)
    # # stores password
    # password = models.CharField(_(""), max_length=50)


    # def __str__(self):
    #     return self.name



class Clan(models.Model):
    user = models.ForeignKey(User, verbose_name=(""), on_delete=models.CASCADE)
    clan_name = models.CharField((""), max_length=50)
    content = models.CharField((""), max_length=50)
    image_url = models.CharField((""), max_length=50)
    discord_url = models.CharField((""), max_length=50)
    website_url = models.CharField((""), max_length=50)
    # match = models.ForeignKey("app.Model", verbose_name=(""), on_delete=models.CASCADE)