from django import forms
from .models import Laboratorio

class LaboratorioForm(forms.ModelForm):
    class Meta:
        model = Laboratorio
        fields = ['nombre', 'ciudad', 'pais']  
        labels = {  # Etiquetas personalizadas para los campos
            'nombre': 'Nombre',
            'ciudad': 'Ciudad',
            'pais': 'País',
        }
        widgets = {  # Widgets personalizados para modificar apariencia o comportamiento
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese el Nombre del laboratorio'}),
            'ciudad': forms.TextInput(attrs={'placeholder': 'Ingrese la Ciudad del laboratorio'}),
            'pais': forms.TextInput(attrs={'placeholder': 'Ingrese el Pais del laboratorio'}),
        }
