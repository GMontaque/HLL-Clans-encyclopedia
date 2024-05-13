from django import forms
from clan_pages.models import Clan
from.models import Match
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit

class ClamMatchForm(forms.Form):
    Username = forms.CharField()
    Your_Clan = forms.ModelChoiceField(queryset=Clan.objects.all())
    Enemy_Clan = forms.ModelChoiceField(queryset=Clan.objects.all())
    game_type = forms.ChoiceField(choices=[(tag, tag) for tag in Match.objects.values_list('game_type', flat=True).distinct()])
    match_date = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)    
    # is_accepted field

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'post'
    #     self.helper.add_input(Submit('submit', 'Submit'))