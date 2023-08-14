from django.db import models
from Produse.models import Produs



class Order(models.Model):
    '''Class to costruct a model for each order'''

    date_created = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)

    def order_summary(self):
        produse = self.orderitem_set.all()
        return sum([produs.quantity for produs in produse])


class OrderItem(models.Model):
    '''Class to construct a model for each product in a order'''


    product = models.ForeignKey(Produs, on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


    def __str__(self):
        return self.product.nume



