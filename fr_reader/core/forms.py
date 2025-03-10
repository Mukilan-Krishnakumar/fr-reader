from django import forms


class TranslateForm(forms.Form):
    url = forms.URLField(label="URL")
