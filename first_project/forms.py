from django import forms

class StrForm(forms.Form):
    text = forms.CharField(label="Введите строку:", max_length=100)


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=20)
    password = forms.CharField(label="Password", max_length=20)
