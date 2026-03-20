from django.db import models


class Garagem(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    criada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    garagem = models.ForeignKey(
        Garagem,
        on_delete=models.CASCADE,
        related_name='veiculos'
    )
    vin = models.CharField(max_length=30)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano_modelo = models.CharField(max_length=20, blank=True)
    fabricante = models.CharField(max_length=100, blank=True)
    tipo_veiculo = models.CharField(max_length=100, blank=True)
    observacao = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.marca} {self.modelo} ({self.vin})'