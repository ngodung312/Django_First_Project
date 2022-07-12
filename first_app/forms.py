from django import forms
from django.core import validators
from first_app.models import UserInfo

class UserForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter name"}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Enter email"}),
            'verify_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Enter email again"}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Enter text"}),
        }      

        