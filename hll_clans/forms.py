from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    clan_rep = forms.BooleanField(label="Clan Rep", required=False)

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.clan_rep = self.cleaned_data['clan_rep']
        user.save()
        return user
    