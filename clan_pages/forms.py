from django import forms
from .models import Clan

class CreateClan(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea, required=True)
    image_url = forms.CharField(required=False)
    class Meta:
        model = Clan
        fields = ['clan_name', 'content', 'image_url', 'discord_url', 'website_url']