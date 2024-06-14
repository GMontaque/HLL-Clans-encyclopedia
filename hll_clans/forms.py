from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    clan_rep = forms.BooleanField(label="Clan Rep", required=False)
    memorable_name = forms.CharField(label="Memorable Name", max_length=100)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.clan_rep = self.cleaned_data['clan_rep']
        user.save()
        user.profile.memorable_name = self.cleaned_data['memorable_name']
        user.profile.save()
        return user