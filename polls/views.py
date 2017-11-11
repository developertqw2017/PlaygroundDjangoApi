from django.http import HttpResponse
from django.shortcuts import render
from datetime import date, datetime
from polls.models import playground,ticket,project
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

def search_project(request,name):
    sear = playground.objects.get(proname = name)
    sear = sear.__delattr__('_state')
    return HttpResponse(json.dumps(sear.__dict__))

def search_comment(request,name):
    sear = project.objects.get(proname = name)
    sear_comment = comment.objects.get(Cprojetct = sear.Pid)
    sear_comment = sear.__delattr__('_state')
    search_comment = search_comment.__delattr__('Ctime')
    return HttpResponse(json.dumps(search_comment.__dict__))
