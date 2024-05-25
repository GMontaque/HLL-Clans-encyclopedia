from django import forms
from .models import Notification

class CreateNotification(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea, required=True)
    class Meta:
        model = Notification
        fields = ['content']

    def __init__(self, *args, **kwargs):
        super(CreateNotification, self).__init__(*args, **kwargs)
        if 'initial' in kwargs:
            for field in ['issuer', 'receiver', 'clan']:
                self.fields[field].widget = forms.HiddenInput()