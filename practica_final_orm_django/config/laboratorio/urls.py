from django.urls import path
from . import views

app_name = 'laboratorio'

urlpatterns = [
    path('', views.listar_laboratorios, name='listar_laboratorios'),
    path('agregar/', views.agregar_laboratorio, name='agregar_laboratorio'),
    path('editar/<int:pk>/', views.editar_laboratorio, name='editar_laboratorio'),
    path('eliminar/<int:pk>/', views.eliminar_laboratorio, name='eliminar_laboratorio'),
]
