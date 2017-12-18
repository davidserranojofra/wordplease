from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView

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
                redirigir_a = request.GET.get('next', 'pagina_inicio')
                return redirect(redirigir_a)
            else:
                messages.error(request, 'Usuario incorrecto o inactivo')
        return render(request, 'login_formulario.html', {'form': form})


class LogoutView(View):

    def get(self, request):
        django_logout(request)
        return redirect('pagina_login')


def signup(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            django_login(request, user)
            return redirect('pagina_inicio')
    else:
        form = RegistroForm()
    return render(request, 'signup.html', {'form': form})


class ListadoBlogs(ListView):

    model = User
    template_name = 'listado_blogs_usuarios.html'
