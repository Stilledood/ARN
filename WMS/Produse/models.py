from django.db import models
from Depozit.models import Raft



class Producator(models.Model):
    '''Class to define a model for producer objects'''

    nume = models.CharField(max_length=250)
    tara_de_origine = models.CharField(max_length=200)
    persoana_contact = models.CharField(max_length=100, blank=True)
    telefon_persoana_contact = models.CharField(max_length=30, blank=True)
    email_persoana_contact = models.CharField(max_length=50, blank=True)

    class Meta:
        ordering = ['nume']

    def __str__(self):
        return self.nume



class Produs(models.Model):
    '''Class to define a model for product object'''

    cod_produs = models.CharField(max_length=50, primary_key=True)
    nume = models.CharField(max_length=200, blank=False)
    inaltime = models.IntegerField()
    latime = models.IntegerField()
    lungime = models.IntegerField()
    producator = models.ForeignKey(Producator, on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ['nume']

    def __str__(self):
        return self.nume


class ProductSet(models.Model):
    '''Class to define a model for products sets-connects products to shelvs'''

    produs = models.ForeignKey(Produs, on_delete=models.DO_NOTHING)
    cantitate = models.IntegerField(blank=False)
    raft = models.ForeignKey(Raft, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.produs.nume





