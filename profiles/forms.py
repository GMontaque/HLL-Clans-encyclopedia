from django import forms
from django.contrib.auth.models import User
from .models import UserProfile

class PasswordResetRequestForm(forms.Form):
    email = forms.EmailField(label="Email", max_length=254)
    verification_value = forms.CharField(
        label="Memorable Name", max_length=100
    )

    def clean_verification_value(self):
        value = self.cleaned_data.get('verification_value')
        email = self.cleaned_data.get('email')

        if email:
            try:
                user = User.objects.get(email=email)
                user_profile = UserProfile.objects.get(user=user)
                if value != user_profile.memorable_name:
                    raise forms.ValidationError("Verification value is incorrect.")
            except (User.DoesNotExist, UserProfile.DoesNotExist):
                raise forms.ValidationError("No account found with this email address.")
        return value

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        if email and not User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "No account found with this email address."
            )
        return cleaned_data

class PasswordChangeForm(forms.Form):
    username = forms.CharField(
        label="Username",
        max_length=150,
        widget=forms.TextInput(attrs={'readonly': 'readonly'})
    )
    new_password = forms.CharField(
        label="New Password",
        widget=forms.PasswordInput()
    )
