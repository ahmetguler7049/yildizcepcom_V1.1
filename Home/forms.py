from django import forms

class emailFormu(forms.Form):
    emailField = forms.EmailField(
        required=True,
        label='E-Posta Adresi',
    )
    subject = forms.CharField(
        max_length=200,
        label='Konu',
    )
    message = forms.CharField(
        label="Mesajınız...",
        widget=forms.Textarea()
    )
