from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User




class LoginForm(forms.Form):

    login_nombre_usuario = forms.CharField(label='Usuario')
    login_password = forms.CharField(widget=forms.PasswordInput(), label='Contraseña')



class RegistroForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, label='Nombre')
    last_name = forms.CharField(max_length=30, label='Apellidos')
    email = forms.EmailField(max_length=254)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )