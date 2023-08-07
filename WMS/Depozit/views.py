from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse

from .models import Raft

class RaftDetails(View):
    '''Class to construct a view to display all products from a shelf'''

    model_class = Raft

    def get(self,request):

        raft = self.model_class.objects.all()
        context = {}
        for r in raft:
            raft_inventar = {}
            for set_produs in r.productset_set.all():
                if set_produs.produs.nume not in raft_inventar:
                    raft_inventar[set_produs.produs.nume] = set_produs.cantitate
                else:
                    raft_inventar[set_produs.produs.nume] = raft_inventar[set_produs.produs.nume] + set_produs.cantitate
            context[r.nume] = raft_inventar
        return JsonResponse(context)

