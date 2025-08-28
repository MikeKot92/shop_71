from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (AuthenticationForm, UserChangeForm,
                                       UserCreationForm)

from .tasks import send_email_verification


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    image = forms.ImageField(required=False, widget=forms.FileInput(attrs={
        'class': 'custom-file-input',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'readonly': True,
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'readonly': True,
    }))

    class Meta:
        model = get_user_model()
        fields = (
            'image',
            'username',
            'first_name',
            'last_name',
            'email',
        )


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Логин',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Пароль',
    }))

    class Meta:
        model = get_user_model()
        fields = (
            'username',
            'password',
        )


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите имя',
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите фамилию',
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите имя пользователя',
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите адрес эл. почты',
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите пароль',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Подтвердите пароль',
    }))

    class Meta:
        model = get_user_model()
        fields = (
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super().save(commit=True)
        send_email_verification.delay(user.id)
        return user
