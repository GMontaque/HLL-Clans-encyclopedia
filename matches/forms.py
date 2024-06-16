from django import forms
from .models import Match
from clan_pages.models import Clan


class ClamMatchForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea, required=True)
    match_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'})
    )

    class Meta:
        model = Match
        fields = ['invitee_clan', 'game_type', 'match_date', 'message']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        if self.user and not self.user.is_superuser:
            self.fields['invitee_clan'].queryset = Clan.objects.exclude(
                user=self.user
            )
        else:
            self.fields['invitee_clan'].queryset = Clan.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        invitee_clan = cleaned_data.get('invitee_clan')
        if self.user and not self.user.is_superuser:
            inviter_clan = Clan.objects.filter(user=self.user).first()
            if invitee_clan == inviter_clan:
                self.add_error(
                    'invitee_clan',
                    "You cannot request a game against your own clan."
                )
        return cleaned_data
