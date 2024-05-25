from django import forms
from .models import Match

class ClamMatchForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea, required=True)
    match_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    class Meta:
        model = Match
        fields = ['inviter_clan', 'invitee_clan', 'game_type', 'match_date','message']
