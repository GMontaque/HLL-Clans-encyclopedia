from allauth.account.forms import SignupForm
from django import forms
from .models import UserProfile

class CustomSignupForm(SignupForm):
    clan_rep = forms.BooleanField(required=False, label='Are you a clan representative?')

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user_profile = UserProfile.objects.get(user=user)
        user_profile.clan_rep = self.cleaned_data.get('clan_rep')
        user_profile.save()
        return user  