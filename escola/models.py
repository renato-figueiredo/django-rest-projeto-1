from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()

    def __str__(self):
        """
        Retorna uma representação de string do objeto.

        :return: A representação de string do objeto, que é o valor do atributo 'nome'.
        :rtype: str
        """
        return self.nome

class Curso(models.Model):
    NIVEL = (
        ('B', 'Básico'),
        ('I', 'Intermediário'),
        ('A', 'Avançado'),
    )
    codigo_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(max_length=1, choices=NIVEL, blank=False, null=False, default='B')

    def __str__(self):
        """
        Um método para retornar a descrição do objeto como uma string.

        :return: A representação de string do objeto, que é o valor do atributo 'nome'.
        :rtype: str
        """
        return self.descricao
    
class Matricula(models.Model):
    PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
    )
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    periodo = models.CharField(max_length=1, choices=PERIODO, blank=False, null=False, default='M')