from django import forms
from custom_admin.models import User


class LoginUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'portfolio_site', 'profile_pic')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter username", 'aria-describedby': "usernameHelp"}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Enter email"}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Enter password"}),
            'portfolio_site': forms.URLInput(attrs={'class': 'form-control', 'placeholder': "Enter portfolio link"}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control custom-file-input'}),
        }