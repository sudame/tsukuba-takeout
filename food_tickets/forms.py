from django import forms


class PaymentForm(forms.Form):
    payjp_token = forms.CharField(max_length=256)

