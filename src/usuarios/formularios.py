from django import forms
from django.forms import ModelForm
from usuarios.models import Post


class LoginForm(forms.Form):

    login_nombre_usuario = forms.CharField(label='Usuario')
    login_password = forms.CharField(widget=forms.PasswordInput(), label='Contraseña')



class RegistroForm(ModelForm):

    class Meta:
        model: Post
        fields: '__all__'