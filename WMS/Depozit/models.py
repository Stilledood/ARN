from django.db import models


class Depozit(models.Model):
    '''Class to define a model for warehouse objects'''

    nume = models.CharField(max_length=200, blank=False)
    adresa = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.nume



class Raft(models.Model):
    '''Class to define a model for all the warehouse shelves'''

    nume = models.CharField(max_length=10, blank=False)
    depozit = models.ForeignKey(Depozit, on_delete=models.CASCADE)

    class Meta:
        ordering = ['nume']

    def __str__(self):
        return self.nume

