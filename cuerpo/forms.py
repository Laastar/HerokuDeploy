from django import forms
from .models import Post, User, Logeado, HacerCita, Opiniones, Recuperacion

class PostFormulario(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('titulo', 'texto')

class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        labels = {
            'username' : "Nombre de usuario",
            'first_name': "Nombre(s)",
            'last_name': "Apellido(s)",
            'email': "Correo electronico",
            'password1': "Contraseña",
            'password2': "Confirmacion de contraseña",
        }
        widgets = {
            'password2' : forms.PasswordInput(),
            'password1' : forms.PasswordInput(),
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = Logeado
        fields = ('username', 'password')
        labels = {
            'username': "Nombre de usuario",
            'password': "Contraseña",
        }
        widgets = {
            'password' : forms.PasswordInput()
        }

class CitasForm(forms.ModelForm):
    class Meta:
        model = HacerCita
        fields = ['dia', 'hora', 'servicio']
        labels = {
            'dia': 'Dia',
            'hora': 'Hora',
            'servicio': 'Serivico',
        }
        widgets = {
            'dia': forms.SelectDateWidget,
            'hora': forms.TimeInput,
        }

class OpinionForm(forms.ModelForm):
    class Meta:
        model = Opiniones
        fields = ['texto', 'terminos']
        labels = {
            'texto': 'Escribe tu opinion',
            'terminos': 'Acepto terminos y condiciones',
        }
        widgets = {
            'texto': forms.Textarea,
            'terminos': forms.CheckboxInput()
        }

class RecuperarForm(forms.ModelForm):
    class Meta:
        model = Recuperacion
        fields = ['email']
        labels = {
            'email' : 'Escribe tu correo electronico'
        }