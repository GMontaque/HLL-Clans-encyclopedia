from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit

class CreateClan(forms.Form):
    Clan_Name = forms.CharField()
    Content = forms.CharField(widget=forms.Textarea)
    Images = forms.EmailField()
    Discord = forms.CharField()
    Website = forms.CharField()

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'post'
    #     self.helper.add_input(Submit('submit', 'Submit'))