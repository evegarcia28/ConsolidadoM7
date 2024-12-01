from django.shortcuts import render, get_object_or_404, redirect
from .models import Laboratorio
from .forms import LaboratorioForm

def listar_laboratorios(request):
    laboratorios = Laboratorio.objects.all()
    return render(request, 'laboratorio/listar_laboratorios.html', {'laboratorios': laboratorios})

def agregar_laboratorio(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('laboratorio:listar_laboratorios')
    else:
        form = LaboratorioForm()
    return render(request, 'laboratorio/agregar_laboratorio.html', {'form': form})

def editar_laboratorio(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('laboratorio:listar_laboratorios')
    else:
        form = LaboratorioForm(instance=laboratorio)
    return render(request, 'laboratorio/agregar_laboratorio.html', {'form': form})

def eliminar_laboratorio(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('laboratorio:listar_laboratorios')
    return render(request, 'laboratorio/eliminar_laboratorio.html', {'laboratorio': laboratorio})

