from django import forms
from .models import Publicacion
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')

class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class PublicacionForm(forms.ModelForm):
    class Meta:
        model = Publicacion
        fields = ['titulo', 'subtitulo', 'contenido', 'imagen']  
        widgets = {
            'titulo': forms.TextInput(attrs={
                'placeholder': 'Ej: Mi primera experiencia con Django fue...',
                'class': 'form-control'
            }),
            'subtitulo': forms.TextInput(attrs={
                'placeholder': 'Ej: No me esperaba que...',
                'class': 'form-control'
            }),
            'contenido': forms.Textarea(attrs={
                'placeholder': 'Describe tu experiencia, por ejemplo: Me pase la noche entera tratando de resolver este error...',
                'class': 'form-control',
                'rows': 5
            }),
            'imagen': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
            }),
        }