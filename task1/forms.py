from django import forms

# Create your views here.


class ContactForm(forms.Form):
    username = forms.CharField(max_length=30, label='Ваше имя')
    password = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Ваш пароль')
    repeat_password = forms.CharField(min_length=8, widget=forms.PasswordInput, label='Повторите пароль')
    age = forms.IntegerField(label='Ваш возраст')