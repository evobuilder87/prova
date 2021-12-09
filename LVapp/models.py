from django.db import models

# Create your models here.
class LVapp(models.Model):
    immagine = models.ImageField()
    nome = models.CharField(max_length=20)
    prezzo = models.FloatField()
    
    #Comando usato per rinominare l'oggetto inserito nel DB con il nome inserito nella classe
    def __str__(self):
        return self.nome