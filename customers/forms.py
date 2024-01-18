from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True),
    last_name = forms.CharField(max_length=30, required=True),
    email = forms.EmailField(max_length=100, required=True),

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)


class ChangeUserDataForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',)
