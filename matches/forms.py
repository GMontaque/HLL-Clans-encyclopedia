from django import forms
from .models import Match
from clan_pages.models import Clan

class ClamMatchForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea, required=True)
    match_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))

    class Meta:
        model = Match
        fields = ['invitee_clan', 'game_type', 'match_date', 'message']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if user and not user.is_superuser:
            self.fields['invitee_clan'].queryset = Clan.objects.exclude(user=user)
        else:
            self.fields['invitee_clan'].queryset = Clan.objects.all()
