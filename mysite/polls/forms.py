from django.forms import ModelForm
from .models import UsuarioInquilo

class InquilinoForm(ModelForm):
    class Meta:
        model = UsuarioInquilo
        fields = ['nombre','curp','piso','departamento','telefono', 'correo']