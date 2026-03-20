from django.shortcuts import render, redirect, get_object_or_404
from .models import Garagem, Veiculo
from .forms import GaragemForm, VeiculoForm


def home(request):
    return render(request, 'garagem/home.html')


def listar_garagens(request):
    garagens = Garagem.objects.all().order_by('-criada_em')
    return render(request, 'garagem/garagens/listar.html', {'garagens': garagens})


def criar_garagem(request):
    form = GaragemForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_garagens')
    return render(request, 'garagem/garagens/form.html', {'form': form, 'titulo': 'Nova garagem'})


def editar_garagem(request, pk):
    garagem = get_object_or_404(Garagem, pk=pk)
    form = GaragemForm(request.POST or None, instance=garagem)
    if form.is_valid():
        form.save()
        return redirect('listar_garagens')
    return render(request, 'garagem/garagens/form.html', {'form': form, 'titulo': 'Editar garagem'})


def excluir_garagem(request, pk):
    garagem = get_object_or_404(Garagem, pk=pk)
    if request.method == 'POST':
        garagem.delete()
        return redirect('listar_garagens')
    return render(request, 'garagem/garagens/excluir.html', {'garagem': garagem})


def listar_veiculos(request):
    veiculos = Veiculo.objects.select_related('garagem').all().order_by('-criado_em')
    return render(request, 'garagem/veiculos/listar.html', {'veiculos': veiculos})


def criar_veiculo(request):
    form = VeiculoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_veiculos')
    return render(request, 'garagem/veiculos/form.html', {'form': form, 'titulo': 'Novo veículo'})


def editar_veiculo(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    form = VeiculoForm(request.POST or None, instance=veiculo)
    if form.is_valid():
        form.save()
        return redirect('listar_veiculos')
    return render(request, 'garagem/veiculos/form.html', {'form': form, 'titulo': 'Editar veículo'})


def excluir_veiculo(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    if request.method == 'POST':
        veiculo.delete()
        return redirect('listar_veiculos')
    return render(request, 'garagem/veiculos/excluir.html', {'veiculo': veiculo})