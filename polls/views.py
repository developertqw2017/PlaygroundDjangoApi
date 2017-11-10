from django.http import HttpResponse
from django.shortcuts import render
from datetime import date, datetime
from polls.models import playground,ticket
import json
def search_playground(request,name):
    sear = playground.objects.get(Pname=name)
    tem = sear;
    tem.__delattr__('Popentime')
    tem.__delattr__('_state')
    resp = json.dumps(tem.__dict__)
    return HttpResponse(resp)

def search_ticket(request,name):
    sear = playground.objects.get(Pname="wuhanhuanlegu")
    qq = ticket.objects.get(Tid=sear.Pid)
    qq.__delattr__('Tdatetime')
    qq.__delattr__('_state')
    resp = json.dumps(qq.__dict__)
    return HttpResponse(resp)
