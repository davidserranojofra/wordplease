from django import forms


class LoginForm(forms.Form):

    login_nombre_usuario = forms.CharField(label='Usuario')
    login_password = forms.CharField(widget=forms.PasswordInput(), label='Contraseña')



class RegistroForm(forms.Form):

    rNombre = forms.CharField(label='Nombre')
    rApellidos = forms.CharField(label='Apellidos')
    rNombreUsuario = forms.CharField(label='Nombre de usuario')
    rEmail = forms.EmailField(label='Email')
    rContrasenya = forms.CharField(label='Contraseña')