from django import forms


# This is not a contact form and has nothing related with any model
class ContactForm(forms.Form):
    name = forms.CharField(required=False,)
    surname = forms.CharField(label='Soyadınız', required=False,)
    email = forms.EmailField(label='E-Posta Adresiniz')
    message = forms.CharField(label='Mesajınız', widget=forms.Textarea)
