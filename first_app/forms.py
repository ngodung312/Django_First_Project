from django import forms
from django.core import validators
from first_app.models import User

class UserForm(forms.ModelForm):
    # name = forms.CharField()
    # email = forms.EmailField()
    # verify_email = forms.EmailField(label='Enter your email again:')
    # text = forms.CharField(widget=forms.Textarea)

    # def clean(self):
    #     all_clean_data = super().clean()
    #     email = all_clean_data['email']
    #     vmail = all_clean_data['verify_email']

    #     if email != vmail:
    #         raise forms.ValidationError("Make sure Emails match!")

    class Meta:
        model = User
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter name"}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Enter email"}),
            'verify_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Enter email again"}),
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Enter text"}),
        }

    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     vmail = self.cleaned_data['verify_email']

    #     if email != vmail:
    #         raise forms.ValidationError("MAKE SURE EMAILS MATCH!")       

        