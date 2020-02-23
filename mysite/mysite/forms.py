from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    emal = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)
    ip_addresse = forms.GenericIPAddressField()
