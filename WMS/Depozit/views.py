from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.template.loader import render_to_string

from Produse.models import Produs
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


class DepozitDetails(View):
    '''Class to display only the available products'''

    model_class = Produs
    def get(self,request):

        url_patterns = request.GET.get('q')
        lista_produse = []
        if url_patterns:
            produse = self.model_class.objects.filter(nume__icontains=url_patterns)
            produse = self.model_class.objects.filter(cod_produs__icontains=url_patterns)
        else:
            produse = self.model_class.objects.all()

        for pr in produse:
            dict_produs = {}
            if pr.productset_set.count():
                dict_produs['cod'] = pr.cod_produs
                dict_produs['nume'] = pr.nume
                for prs in pr.productset_set.all():
                    if 'cantitate' not in dict_produs:
                        dict_produs['cantitate'] = prs.cantitate
                    else:
                        dict_produs['cantitate'] = dict_produs['cantitate'] + prs.cantitate
                    if 'raft' not in dict_produs:
                        dict_produs['raft'] = {prs.raft.nume:prs.cantitate}
                    else:
                        if prs.raft.nume not in dict_produs['raft'].keys():
                            dict_produs['raft'][prs.raft.nume] = prs.cantitate
                        else:
                            dict_produs['raft'][prs.raft.nume] = dict_produs['raft'][prs.raft.nume] + prs.cantitate
            if len(dict_produs) > 0:
                lista_produse.append(dict_produs)
        does_req_accepts_json = request.accepts("aplication/json")
        is_ajax_request = request.headers.get("x-requested_with") == "XMLHttpRequest" and does_req_accepts_json
        if is_ajax_request:
            html = render_to_string(template_name='produse_search_result.html',context={"produse":lista_produse})
            data_dict = {"html_from_view":html}
            return JsonResponse(data=data_dict,safe=False)


        return render(request,template_name='Depozit/depozit_details.html',context={"produse":lista_produse})


