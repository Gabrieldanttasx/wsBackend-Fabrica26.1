from django import forms
from .models import Garagem, Veiculo


class GaragemForm(forms.ModelForm):
    class Meta:
        model = Garagem
        fields = ['nome', 'descricao']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }


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
        widgets = {
            'garagem': forms.Select(attrs={'class': 'form-select'}),
            'vin': forms.TextInput(attrs={'class': 'form-control'}),
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'ano_modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'fabricante': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_veiculo': forms.TextInput(attrs={'class': 'form-control'}),
            'observacao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }