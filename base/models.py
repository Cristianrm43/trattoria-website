from django.db import models

# Create your models here.

class Buy(models.Model):
    id = models.AutoField(primary_key=True, unique=True)  # ID único, normalmente gerado automaticamente pelo Django
    nome = models.CharField(max_length=255)  # Campo para o nome (máximo de 255 caracteres)
    phone = models.CharField(max_length=14)  # Campo para o telefone (máximo de 14 caracteres)
    cpf = models.CharField(max_length=11, unique=True)  # Campo para o CPF (máximo de 14 caracteres e único)
    email = models.EmailField(max_length=255)  # Campo para o email (deve ser um endereço de e-mail válido)

    def __str__(self):
        return self.nome  # Uma representação de string amigável para a classe

    class Meta:
        verbose_name_plural = "Compradores"  # O nome plural para a classe no admin do Django

from django.db import models

class Ticket(models.Model):
    comprador = models.ForeignKey(Buy, on_delete=models.CASCADE)  # Chave estrangeira para a classe MinhaClasse
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()
    restricao_alimentar = models.TextField(blank=True, null=True)  # Campo de texto para restrição alimentar (pode ser em branco)
    TIPO_CHOICES = [
        ('adulto', 'Adulto'),
        ('crianca', 'Criança'),
    ]
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    CONHECIDOS_CETEC_CHOICES = [
        ('aluno', 'Aluno'),
        ('aluno_tecnico', 'Aluno do Técnico'),
        ('professor', 'Professor'),
        ('ninguem', 'Ninguém'),
    ]
    conhecidos_cetec = models.CharField(max_length=15, choices=CONHECIDOS_CETEC_CHOICES)

    def __str__(self):
        return f"{self.nome} ({self.cpf})"

    class Meta:
        verbose_name_plural = "Ingressos"

