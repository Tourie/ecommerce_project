from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import User


class RegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=60, help_text='Обязательное к заполнению поле.')

    class Meta:
        model = User
        fields = {'name', 'username', 'email', 'age', 'password1', 'password2'}

    def clean_username(self):
        if self.is_valid():
            new_username = self.cleaned_data['username'].lower()
            return new_username


class UserAuthentificationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self):
        if self.is_valid():
            username = self.cleaned_data['username'].lower()
            password = self.cleaned_data['password']
            if not authenticate(username=username, password=password):
                raise forms.ValidationError('Invalid login!')


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'username', 'name', 'age')

    def clean_email(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            try:
                user = User.objects.exclude(pk=self.instance.pk).get(email=email)
            except User.DoesNotExist:
                return email
            raise forms.ValidationError(f'Email {user.email} уже используется.')

    def clean_username(self):
        if self.cleaned_data['username'].lower() == 'clean':
            pass
        if self.is_valid():
            username = self.cleaned_data['username']
            try:
                user = User.objects.exclude(pk=self.instance.pk).get(username=username)
            except User.DoesNotExist:
                return username
            raise forms.ValidationError(f'Никнейм {user.username} уже используется.')

    def clean_name(self):
        if self.is_valid():
            name = self.cleaned_data['name']
            return name
