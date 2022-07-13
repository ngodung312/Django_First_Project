from dataclasses import fields
from django import forms
from first_app.models import UserInfo, UserProfile
from django.contrib.auth.models import User


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

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        vmail = cleaned_data.get("verify_email")
        print(email, vmail)
        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")       


class LoginUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter username", 'aria-describedby': "usernameHelp"}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Enter email"}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Enter password"}),
        }


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('portfolio_site', 'profile_pic') 
        widgets = {
            'portfolio_site': forms.URLInput(attrs={'class': 'form-control', 'placeholder': "Enter portfolio link"}),
            'profile_pic': forms.FileInput(attrs={'class': 'form-control custom-file-input'}),
        }
        