from allauth.account.forms import SignupForm
from django import forms
from profiles.models import UserProfile

class CustomSignupForm(SignupForm):
    clan_rep = forms.BooleanField(label="Clan Rep", required=False)
    memorable_name = forms.CharField(label="Memorable Name", max_length=100)

    def save(self, request):
        print(request)
        user = super(CustomSignupForm, self).save(request)
        userprofile = UserProfile(user=user, memorable_name=self.cleaned_data['memorable_name'], clan_rep = self.cleaned_data['clan_rep']  )
        userprofile.save()

        return user