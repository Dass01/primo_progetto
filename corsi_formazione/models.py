from django.db import models
from datetime import datetime

# Create your models here.

class Corso(models.Model):
    """modello gerarchico di un giornalista"""
    titolo=models.CharField(max_length=20)
    descrizione=models.TextField()
    data_inizio=models.DateField(default=datetime.now(), blank=True)
    data_fine=models.DateField(default=datetime.now(), blank=True)
    posti_disponibili=models.IntegerField()

    def __str__ (self):
        return self.titolo
    
    class Meta:
        verbose_name="Corso"
        verbose_name_plural="Corsi"
