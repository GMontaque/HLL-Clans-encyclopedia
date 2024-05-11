from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit

class create_clan(forms.Form):
    Clan_Name = forms.CharField()
    Content = forms.CharField()
    Images = forms.EmailField()
    Discord = forms.CharField(widget=forms.Textarea)
    Website = forms.CharField(widget=forms.Textarea)

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'post'
    #     self.helper.add_input(Submit('submit', 'Submit'))