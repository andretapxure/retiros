from django.db import models

# Create your models here.


class Participante(models.Model):
    SEXO = (
       (1, 'Masculino'),
       (2, 'Feminino'),
   )
    ESTADO_CIVIL = (
        (1, 'Casado Civil'),
        (2, 'Casado Religioso'),
        (3, 'Sacramento'),
        (4, 'Batismo'),
        (5, 'Eucaristia'),
        (6, 'Crisma'),
        
    )
    nome = models.CharField(db_column='nome', max_length=100, blank=False)
    cpf = models.CharField(db_column='cpf', max_length=14, blank=False, unique=True)
    nascimento = models.DateField(db_column='nascimento', blank=True)
    sexo = models.SmallIntegerField(db_column='sexo', choices=SEXO, blank=False)
    estadocivil = models.SmallIntegerField(db_column='estadocivil', choices=ESTADO_CIVIL, blank=False)
  
    class Meta:
        db_table = 'participante'
        verbose_name = 'Participantes'
        verbose_name_plural = 'Participantes'

    def __unicode__(self):
        return self.nome if self.nome else ''

    def __str__(self):
        return self.nome if self.nome else ''



class Retiro(models.Model):
    nome = models.CharField(db_column='nome', max_length=100, blank=False)
    data = models.DateField(blank=False)
    descricao = models.TextField(blank=True)
    class Meta:
        db_table = 'retiro'
        verbose_name = 'Retiro'
        verbose_name_plural = 'Retiros'

    def __unicode__(self):
        return self.nome if self.nome else ''

    def __str__(self):
        return self.nome if self.nome else ''


class Participacao(models.Model):
    retiro = models.ForeignKey(Retiro, on_delete=models.PROTECT )
    participante = models.ForeignKey(Participante, on_delete=models.CASCADE)
    class Meta:
        db_table = 'participacao'
        verbose_name = 'Participacao'
        verbose_name_plural = 'Participacoes'
