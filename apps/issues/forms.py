from django import forms
from apps.issues.models import Issue

__author__ = 'petry'


class IssueForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': u'Issue Title',
                'class': 'form-control'
            }
        )
    )
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': u'Description',
                'class': 'form-control'
            }
        )
    )

    class Meta:
        model = Issue

