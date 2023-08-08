from django import forms


class ProductoFormulario(forms.Form):
    nombre_producto = forms.CharField(required=True, max_length=64)
    precio = forms.IntegerField(required=True, max_value=50000)
