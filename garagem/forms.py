from django import forms
from .models import Garagem, Veiculo


class GaragemForm(forms.ModelForm):
    class Meta:
        model = Garagem
        fields = ['nome', 'descricao']


class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = [
            'garagem',
            'vin',
            'marca',
            'modelo',
            'ano_modelo',
            'fabricante',
            'tipo_veiculo',
            'observacao',
        ]