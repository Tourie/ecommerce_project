from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import User


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=60, help_text='Обязательное к заполнению поле.')

    class Meta:
        model = User
        fields = {'name', 'username', 'email', 'age', 'password1', 'password2'}


class UserAuthentificationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError('Invalid login!')
