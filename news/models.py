from django.db import models
from datetime import datetime

# Create your models here.

class Giornalista(models.Model):
    """modello gerarchico di un giornalista"""
    nome=models.CharField(max_length=20)
    cognome=models.CharField(max_length=20)
    dataNascita=models.DateField(default=datetime.now(), blank=True)

    def __str__ (self):
        return self.nome+" "+self.cognome
    
    class Meta:
        verbose_name="Giornalista"
        verbose_name_plural="Giornalisti"
    
class Articolo(models.Model):
    """il modello gerarchico di un articolo di news"""
    titolo=models.CharField(max_length=100)
    contenuto=models.TextField()
    giornalista=models.ForeignKey(Giornalista, on_delete=models.CASCADE, related_name="articoli")
    visualizzazioni=models.SmallIntegerField(default=0)
    dataPubblicazione=models.DateField(default=datetime.now(), blank=True)

    def __str__(self):
        return self.titolo
    
    class Meta:
        verbose_name="Articolo"
        verbose_name_plural="Articoli"
        