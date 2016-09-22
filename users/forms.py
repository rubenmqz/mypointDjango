from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.password_validation import validate_password
from django.forms import ModelForm
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    username = forms.CharField(label="Nombre de usuario")
    pwd = forms.CharField(label="Contraseña", widget=forms.PasswordInput())


class SignupForm(UserCreationForm):
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

        def clean_first_name(self):
            """
            Valida que el nombre esté relleno
            :return: el valor del campo
            """
            cleaned_data = super().clean().get('first_name')

            if cleaned_data is '':
                raise ValidationError("Este campo es obligatorio")
            return cleaned_data

        def clean_last_name(self):
            """
            Valida que el apellido esté relleno
            :return: el valor del campo
            """
            cleaned_data = super().clean().get('last_name')

            if cleaned_data is '':
                raise ValidationError("Este campo es obligatorio")
            return cleaned_data


class SignupForm1(ModelForm):

    class Meta:
        model = User
        fields = ["first_name", "last_name", "username", "email", "password"]


    def clean_first_name(self):
        """
        Valida que el nombre esté relleno
        :return: el valor del campo
        """
        cleaned_data = super().clean().get('first_name')

        if cleaned_data is '':
            raise ValidationError("Debes indicar tu nombre")
        return cleaned_data

    def clean_last_name(self):
        """
        Valida que el apellido esté relleno
        :return: el valor del campo
        """
        cleaned_data = super().clean().get('last_name')

        if cleaned_data is '':
            raise ValidationError("Debes indicar tu apellido")
        return cleaned_data

    def clean_email(self):
        """
        Valida que el email esté relleno
        :return: el valor del campo
        """
        cleaned_data = super().clean().get('email')

        if cleaned_data is '':
            raise ValidationError("Debes indicar tu e-mail")
        return cleaned_data

    def clean_password(self):
        """
        Valida que el password cumpla los validadores indicados en settings
        :return: el valor del campo
        """
        cleaned_data = super().clean().get('password')

        validate_password(cleaned_data)

        return cleaned_data