from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password']
        #exclude

        label={
            'password':'Password'
        }

    # def clean_email(self):
    #     if.self.cleaned_data['email'].endswith('@gmail.com'):
    #         return self.cleaned_data['email']
    #     else:
    #         raise ValidationError("Email not valid")
    def save(self):
        password=self.cleaned_data.pop('password')
        u=super().save()
        u.set_password(password)
        u.save()
        return u
