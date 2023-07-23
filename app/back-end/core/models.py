from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, id_user, password=None):
        if not id_user:
            raise ValueError("O campo 'id_user' é obrigatório.")

        user = self.model(id_user=id_user)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id_user, password=None):
        user = self.create_user(id_user, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id_user = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'id_user'

    def __str__(self):
        return self.id_user

class Professor(models.Model):
    nome = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10)
    formacao = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Sala(models.Model):
    nome = models.CharField(max_length=100)
    capacidade = models.IntegerField()
    bloco = models.CharField(max_length=100)


    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Alocacao(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    horario = models.TimeField()
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    bloco = models.CharField(max_length=100)
    semana = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.professor} - {self.curso}'


class Horario(models.Model):
    DIAS_DA_SEMANA = [
        ('segunda', 'Segunda-feira'),
        ('terca', 'Terça-feira'),
        ('quarta', 'Quarta-feira'),
        ('quinta', 'Quinta-feira'),
        ('sexta', 'Sexta-feira'),
    ]

    HORARIOS = [
        ('08:00', '08:00'),
        ('10:00', '10:00'),
        ('13:30', '13:30'),
        ('15:30', '15:30'),
    ]

    dia_semana = models.CharField(max_length=10, choices=DIAS_DA_SEMANA)
    horario = models.CharField(max_length=5, choices=HORARIOS)

    def __str__(self):
        return f"{self.get_dia_semana_display()} - {self.horario}"