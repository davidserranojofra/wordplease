from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views import View

from usuarios.formularios import LoginForm, RegistroForm


class LoginView(View):

    def get(self, request):
        contexto = {'form': LoginForm()}
        return render(request, 'login_formulario.html', contexto)

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('login_nombre_usuario')
            password = form.cleaned_data.get('login_password')
            usuario_autenticado = authenticate(username=usuario, password=password)
            if usuario_autenticado and usuario_autenticado.is_active:
                django_login(request, usuario_autenticado)
                return redirect('pagina_inicio')
            else:
                messages.error(request, 'Usuario incorrecto o inactivo')
        return render(request, 'login_formulario.html', {'form': form})

class LogoutView(View):

    def get(self, request):
        django_logout(request)
        return redirect('pagina_login')


class Registro(View):

    def get(self, request):
        form = RegistroForm()
        return render(request, "signup.html", {'form': form})