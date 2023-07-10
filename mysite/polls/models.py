import datetime

from django.db import models
from django.utils import timezone


from django.contrib import admin
#from django.contrib.auth.models import User


class UsuarioInquilo(models.Model):
    nombre = models.CharField(max_length=30)
 #   user = models.ForeignKey(User)
    curp = models.CharField(max_length=30)
     # domicilio
    piso = models.IntegerField()
     # type: Number,
    departamento = models.IntegerField()
     # type: Number,
    telefono = models.CharField(max_length=15)
     # type: String, models.IntegerField()
    correo = models.CharField(max_length=30)
    #  type: String,
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre


class UsuarioVisitante(models.Model):
    nombre = models.CharField(max_length=30)
 #   user = models.ForeignKey(User)
    curp = models.CharField(max_length=30)
     # type: Number,
    telefono = models.IntegerField()
     # type: String,
    correo = models.CharField(max_length=30)
    #  type: String,
    created = models.DateTimeField(auto_now_add=True)
    #inquilino a visitar
    nombre_inquilino = models.CharField(max_length=30)
     # type: Number,
    parentesco = models.CharField(max_length=30)
    


class Question(models.Model):
    # ...
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return self.question_text
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now   

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    # ...
    def __str__(self):
        return self.choice_text