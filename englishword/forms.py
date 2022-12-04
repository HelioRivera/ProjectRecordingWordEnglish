from django import forms


class InsertaPalabras(forms.Form):
    tipo = forms.CharField()
    palabra = forms.CharField()
    significado = forms.CharField()

