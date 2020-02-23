from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField()
    emal = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)
