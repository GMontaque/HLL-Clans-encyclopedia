from django import forms
from .models import Clan


# creates form used to create clan page
class CreateClan(forms.ModelForm):
    # makes content a text area allowing for more text conent
    content = forms.CharField(widget=forms.Textarea, required=True)
    # image is not required for form completion
    # image_url = forms.CharField(required=False)

    class Meta:
        model = Clan

        # the names of the different fields in the form
        fields = ['clan_name', 'content', 'image_url',
                  'discord_url', 'website_url']