from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserLogin(forms.ModelForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-group', 'placeholder': 'Username'}))

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-group', 'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ['username', 'password']


class UserCreation(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-group', 'placeholder': 'Username'}))

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-group', 'placeholder': 'Email'}))

    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-group', 'placeholder': 'Password'}))

    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-group', 'placeholder': 'Repeat Your Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdate(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
