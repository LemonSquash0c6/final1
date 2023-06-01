from django import forms
from .models import User, Login, Datim1, Datim2
from django.utils import timezone


# class LoginForm(forms.Form):
#     username = forms.CharField(label='Username',max_length=30)
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)

class puin(forms.ModelForm):
    class Meta:
        model = Datim1
        fields = ('username',)


class puout(forms.ModelForm):
    class Meta:
        model = Datim2
        fields = ('username',)


class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = ('username', 'password')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('uid', 'name', 'email', 'phone', 'username')
