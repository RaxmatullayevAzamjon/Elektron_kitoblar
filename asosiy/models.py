from django.db import models
from django.contrib.auth.models import User

class Bolim(models.Model):
    nom = models.CharField(max_length=30)
    haqida = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.nom

class Muallif(models.Model):
    ism = models.CharField(max_length=30)
    tirik = models.BooleanField()
    mamlakat = models.CharField(max_length=30)

    def __str__(self):
        return self.ism


class Kitob(models.Model):
    nom = models.CharField(max_length=30)
    muallif = models.ForeignKey(Muallif,on_delete=models.CASCADE)
    yil = models.CharField(max_length=20)
    bolim = models.ForeignKey(Bolim,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rasm = models.FileField()
