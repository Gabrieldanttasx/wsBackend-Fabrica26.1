from django.shortcuts import render, redirect, get_object_or_404
from .models import Garagem, Veiculo
from .forms import GaragemForm, VeiculoForm
from .services import decodificar_vin

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
    data = request.GET or None
    form = VeiculoForm(data or None)

    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_veiculos')

    return render(request, 'garagem/veiculos/form.html', {
        'form': form,
        'titulo': 'Novo veículo'
    })


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


def consultar_vin(request):
    resultado = None
    erro = None

    if request.method == 'POST':
        vin = request.POST.get('vin', '').strip()
        ano_modelo = request.POST.get('ano_modelo', '').strip()

        if not vin:
            erro = 'Digite um VIN.'
        else:
            try:
                resultado = decodificar_vin(vin, ano_modelo)
            except Exception:
                erro = 'Não foi possível consultar a API neste momento.'

    return render(request, 'garagem/consulta_vin.html', {
        'resultado': resultado,
        'erro': erro
    })