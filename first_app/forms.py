from django import forms
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

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        vmail = cleaned_data.get("verify_email")
        print(email, vmail)
        if email != vmail:
            raise forms.ValidationError("MAKE SURE EMAILS MATCH!")       
        