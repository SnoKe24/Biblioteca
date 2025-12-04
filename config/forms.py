from django import forms
from django.forms.widgets import ClearableFileInput
from ckeditor.widgets import CKEditorWidget
from .models import Producto

class CustomClearableFileInput(ClearableFileInput):
    template_name = 'django/forms/widgets/clearable_file_input.html'

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        # Cambiar los textos por defecto
        context['clear_checkbox_label'] = 'Eliminar archivo'
        context['initial_text'] = 'Archivo actual: '
        context['input_text'] = 'Cambiar: '
        return context

class ProductoForm(forms.ModelForm):
    descripcion = forms.CharField(widget=CKEditorWidget(attrs={'class': 'descripcion-ckeditor'}), label="Descripción")

    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'imagen', 'categoria']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'input-nombre'}),
            'precio': forms.NumberInput(attrs={'class': 'input-precio'}),
            'imagen': CustomClearableFileInput(attrs={'class': 'input-imagen'}),
            'categoria': forms.Select(attrs={'class': 'input-categoria'}),
        }