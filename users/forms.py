from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario")
    pwd = forms.CharField(label="Contraseña", widget=forms.PasswordInput())


class SignupForm(UserCreationForm):
        first_name = forms.CharField(required=True, label='Nombre')
        last_name = forms.CharField(required=True, label='Apellido')
        email = forms.EmailField(required=True)

        class Meta:
            model = User
            fields = ["first_name", "last_name", "username", "email", "password1", "password2"]

        def save(self, commit=True):
            user = super().save(commit=False)
            user.email = self.cleaned_data["email"]
            if commit:
                user.save()
            return user


