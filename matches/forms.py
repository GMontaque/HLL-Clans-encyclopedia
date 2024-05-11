from django import forms
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit

class clam_match(forms.Form):
    Username = forms.CharField()
    Your_Clan = forms.CharField()
    Enemy_Clan = forms.CharField()
    game_type = forms.CharField()
    match_date = forms.CharField()
    message = forms.CharField(widget=forms.Textarea)
    # is_accepted field

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'post'
    #     self.helper.add_input(Submit('submit', 'Submit'))