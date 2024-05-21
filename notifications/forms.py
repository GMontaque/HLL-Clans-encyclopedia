from django import forms
from .models import Notification

class CreateNotification(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea, required=True)
    class Meta:
        model = Notification
        fields = ['issuer', 'receiver','clan', 'content', 'status']