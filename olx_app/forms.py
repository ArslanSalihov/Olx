from dataclasses import field
import email
from unicodedata import name
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Наименование',required=True, widget=forms.TextInput(attrs={'class':'form-input'}))
    password = forms.CharField(label='Пароль',required=True, widget=forms.PasswordInput(attrs={'class':'form-input'}))
    email = forms.EmailField(label='E-mail',required=True, widget=forms.TextInput(attrs={'class':'form-input'}))

    class Meta:
        model = User
        fields  = ( 'email', 'username', 'password1')

    def save(self, commit=True):
        user = super().save(commit= False)
        user.email = self.cleaned_data['email']


        if commit:
            user.save()
            return user