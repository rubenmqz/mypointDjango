from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.shortcuts import render, redirect
from django.views import View

from users.forms import LoginForm, SignupForm


class LoginView(View):

    def get(self, request):
        """
        Presenta el formulario de login
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        error_message = ""
        login_form = LoginForm()
        context = {'error': error_message, 'form': login_form}
        return render(request, 'users/login.html', context)

    def post(self, request):
        """
        Gestiona el login de un usuario
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        error_message = ""
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('pwd')
            user = authenticate(username=username, password=password)
            if user is None:
                error_message = "Usuario o contraseña incorrecto"
            else:
                if user.is_active:
                    django_login(request, user)
                    return redirect(request.GET.get('next', 'site_home'))
                else:
                    error_message = "Cuenta de usuario inactiva"
        context = {'error': error_message, 'form': login_form}
        return render(request, 'users/login.html', context)


class LogoutView(View):

    def get(self, request):
        """
        Hace el logout de un usuario y redirige al login
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        if request.user.is_authenticated():
            django_logout(request)
        return redirect('/', 'site_home')


class SignupView(View):

    def get(self, request):
        """
        Presenta el formulario de registro
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        error_message = ""
        signup_form = SignupForm()
        context = {'error': error_message, 'form': signup_form, 'registered': False}
        return render(request, 'users/signup.html', context)

    def post(self, request):
        """
        Gestiona el registro de un nuevo usuario
        :param request: objeto HttpRequest con los datos de la petición
        :return: objeto HttpResponse con los datos de la respuesta
        """
        message = ""
        signup_form = SignupForm(request.POST)
        signup_ok = False
        if signup_form.is_valid():
            new_user = signup_form.save()
            signup_ok = True
            user = authenticate(username=new_user.username, password=signup_form.cleaned_data.get('password1'))

            if user.is_active:
                django_login(request, user)
                message = "Registrado correctamente."
            else:
                message = "Cuenta de usuario inactiva."
        else:
            message = "Form not valid"
        context = {'error': message, 'form': signup_form, 'registered': signup_ok}
        return render(request, 'users/signup.html', context)