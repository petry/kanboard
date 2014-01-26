from django import forms
from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                'placeholder': u'username',
                'class': 'form-control'
            }
        )
    )
    password = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                'placeholder': u'password',
                                'class': 'form-control'

            }
        )
    )