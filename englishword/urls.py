from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('/insertar', views.inserta_palabra)
]
