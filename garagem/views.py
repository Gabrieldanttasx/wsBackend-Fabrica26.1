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