from django.http import HttpResponse
from django.shortcuts import render
from datetime import date, datetime
from polls.models import playground
import json
def search_playground(request,name):
    sear = playground.objects.get(Pname=name)
    tem = sear;
    tem.__delattr__('Popentime')
    tem.__delattr__('_state')
    resp = json.dumps(tem.__dict__)
    return HttpResponse(resp)

def serch_ticket(request,name):
    sear = ticket.objects.get(TplaygroundId)
