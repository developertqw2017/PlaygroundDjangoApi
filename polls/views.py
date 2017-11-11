from django.http import HttpResponse
from django.shortcuts import render
from datetime import date, datetime
from polls.models import playground,ticket,project,userBaseInfo,userticket,Comment,entertainment
import json
def search_playground(request,name):
    sear = playground.objects.get(Pname=name)
    tem = sear;
    tem.__delattr__('Popentime')
    tem.__delattr__('_state')
    resp = json.dumps(tem.__dict__)
    return HttpResponse(resp)

def search_ticket(request,name):
    sear = playground.objects.get(Pname=name)
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

def search_userticket(request,name):
    sear = userBaseInfo.objects.get(Uname=name)
    sear_ticket = userticket.objects.filter(Uid = sear.Uid)
    sear_ticket = [st.__delattr__('_state') for st in sear_ticket]
    sear_ticketid = [ticket.objects.get(Tid = st.Uticket) for st in sear_ticket]
    sear_ticketinfo = [st.__delattr__('_state') for st in sear_ticketid]
    resp1 = json.dumps(sear_ticket.__dict__)
    resp2 = json.dumps(sear_ticketinfo.__dict__)
    return HttpResponse({resp1,resp2})
