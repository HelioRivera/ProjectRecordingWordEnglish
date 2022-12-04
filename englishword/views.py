from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import RegistroPalabra
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime

from .forms import InsertaPalabras

# Create your views here.


def home(request):
    # retorna el listado de todas las palabras
    lista_palabras = RegistroPalabra.objects.all()
    # la variable lista palabras se la enviamos a la plantilla para que sea procesada
    return render(request, "base_gestionpalabras.html", {"lista_palabras": lista_palabras})


def inserta_palabra(request):
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = InsertaPalabras(request.POST)

