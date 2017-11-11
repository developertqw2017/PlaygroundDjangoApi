from django.http import HttpResponse
from django.shortcuts import render
from datetime import date, datetime
from polls.models import playground,ticket,project,userBaseInfo,userticket,Comment,entertainment
import urllib
import json
def search_playground(request,name):
    name = urllib.parse.unquote(name)
    sear = playground.objects.get(Pname=name)
    tem = sear;
    tem.__delattr__('Popentime')
    tem.__delattr__('_state')
    resp = json.dumps(tem.__dict__)
    return HttpResponse(resp)

def search_ticket(request,name):
    name = urllib.parse.unquote(name)
    sear = playground.objects.get(Pname=name)
    qq = sear.ticket_set.all()
    resp3 = [x for x in range(len(qq))]
    d3 = [x for x in range(len(qq))]
    #resp = [x for x in range(len(qq))]
    for x in range(len(qq)):
        qq[x].__delattr__('Tdatetime')
        qq[x].__delattr__('_state')
        qq[x].__delattr__('_TplaygroundId_id_cache')
        d3[x] = qq[x].__dict__
    resp3 = json.dumps(d3)
    return HttpResponse(resp3)

def search_project(request,name):
    name = urllib.parse.unquote(name)
    sear = playground.objects.get(Pname = name)
    sear.__delattr__('_state')
    sear.__delattr__('Popentime')
    return HttpResponse(json.dumps(sear.__dict__))

def search_comment(request,name):
    name = urllib.parse.unquote(name)
    sear = project.objects.get(proname = name)
    sear_comment = Comment.objects.get(Cproject = sear.proid)
    sear_comment = sear.__delattr__('_state')
    search_comment = search_comment.__delattr__('Ctime')
    return HttpResponse(json.dumps(search_comment.__dict__))

def search_userticket(request,name):

    sear = userBaseInfo.objects.get(Uname=name)
    sear_ticket = userticket.objects.filter(Uid = sear.Uid)
    #sear_ticket = [st.__delattr__('_state') for st in sear_ticket]
    sear_ticketid = [ticket.objects.get(Tid=x) for x in [st.Uticket.Tid for st in sear_ticket]]
    for st in range(len(sear_ticketid)):
        sear_ticketid[st].__delattr__('_state')
        sear_ticketid[st].__delattr__('Tdatetime')
    resp2 =[x for x in range(len(sear_ticketid))]
    for st in range(len(resp2)):
        resp2[st] = json.dumps(sear_ticketid[st].__dict__)
    return HttpResponse(resp2)
