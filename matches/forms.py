from django import forms
from .models import Match

# create clan match form
class ClamMatchForm(forms.ModelForm):
    # creates a text box field for messages
    message = forms.CharField(widget=forms.Textarea, required=True)
    # updates match data to a time and date field
    match_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    class Meta:
        model = Match
        # clan match field names
        fields = ['inviter_clan', 'invitee_clan', 'game_type', 'match_date','message']
