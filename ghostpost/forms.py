from django import forms


class BroastForm(forms.Form):

    is_roast = forms.BooleanField()
    content = forms.CharField(max_length=280)
