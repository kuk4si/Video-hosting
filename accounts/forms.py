from django import forms
from django.contrib.auth import authenticate

from .models import User
from django.contrib.auth.hashers import check_password


class UserRegisterForm(forms.ModelForm):

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))
    password2 = forms.CharField(label='Пароль ещё раз', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))

    class Meta:
        model = User
        fields = ('username',)

    """
    Проверка совпадения паролей
    """

    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return data['password']


class UserLoginForm(forms.Form):

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control'
    }))

    """
    Проверка формой на наличие пользователя
    и его состояния (активен или нет (is_active))
    """

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        if username and password:
            qs = User.objects.filter(username=username)
            if not qs.exists():
                raise forms.ValidationError('Пользователь не существует')
            if not check_password(password, qs[0].password):
                raise forms.ValidationError('Неверный пароль')
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Данный пользователь не активен')
        return super().clean(*args, **kwargs)