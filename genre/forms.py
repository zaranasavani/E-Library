# forms.py
from django import forms
from .models import UserProfile
from django.core.exceptions import ValidationError
import datetime

class RegistrationForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'password', 'gender', 'country', 'dob', 'mobile']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        # Password validation logic here
        if len(password) < 8 or not any(char.isupper() for char in password) or \
           not any(char.islower() for char in password) or not any(char.isdigit() for char in password):
            raise ValidationError("Password must be at least 8 characters long, and include uppercase, lowercase, and numeric characters.")
        return password

    def clean_dob(self):
        dob = self.cleaned_data.get('dob')
        if dob >= datetime.date.today():
            raise ValidationError("Date of birth cannot be today or in the future.")
        return dob

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Passwords do not match")
