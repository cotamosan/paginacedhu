from ftplib import MAXLINE
from django import forms 

class craeteNewTask(forms.Form):
    nombre = forms.CharField(label="nombre de la persona", max_length=250)
    apellido = forms.CharField(label="segundo nombre ", max_length=250)

from .models import ImagenGaleria

class ImagenGaleriaForm(forms.ModelForm):
    class Meta:
        model = ImagenGaleria
        fields = ['imagen', 'titulo', 'orden']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['orden'].widget.attrs.update({
            'min': '1',
            'max': '9',
            'class': 'border rounded px-2 py-1 w-full'
        })
        self.fields['imagen'].widget.attrs.update({
            'class': 'block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100'
        })
        self.fields['titulo'].widget.attrs.update({
            'class': 'border rounded px-2 py-1 w-full',
            'placeholder': 'Título opcional'
        })

# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Documento")
    password = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})

        from django import forms
from .models import Administrador

class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = ['documento', 'nombre_completo', 'correo_electronico', 'telefono', 'is_active']
        widgets = {
            'documento': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'correo_electronico': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }