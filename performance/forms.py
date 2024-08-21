from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Student

class StudentRegistrationForm(UserCreationForm):
    class Meta:
        model = Student
        fields = ['username', 'roll_number', 'department', 'password1', 'password2']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
