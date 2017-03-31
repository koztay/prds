from django import forms


# This is a contact form and has nothing related with any model
class ContactForm(forms.Form):
    name = forms.CharField(required=False,)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
