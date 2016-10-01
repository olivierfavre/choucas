from datetime import datetime, timedelta
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.views.generic import ListView
from django.views.generic import DetailView
from gendloc.models import *
from djgeojson.views import GeoJSONLayerView

@login_required
def index(request):
    return HttpResponse("GENDLOC")

@login_required
@permission_required('gendloc.can_add')
#@credit_required
def envoi_sms(request):
    #Vérifier crédit
    #Récupération des paramètres
    user=str(request.user)
    phonenumber = request.GET['tel']
    langue = request.GET['lang']
    validite = request.GET['val']
    modele = request.GET['message']
    #Construire le message
    #Déterminer le SENDER
    sender = 'GENDLOC'
    #Déterminer le texte
    txt = Sms_Model.objects.get(pk=modele).texte
    #ajout entrée dans la table sms
    s = Sms(unite="PG38", utilisateur=user, mod_msg=Sms_Model(int(modele)), tel=phonenumber, validite=int(validite), statut="ENVOI")
    s.save()
    cle = s.id
    #Envoyer le SMS
    #import callr
    #api = callr.Api(settings.CALLR_NAME, settings.CALLR_PWD)
    #result = api.call('sms.send', sender, phonenumber, texte, None)
    #Mise à jour entrée table sms avec statut et hash
    s.statut = "SENT"
    s.envoi_hash = "JVVJHH"
    s.save()
    #Retour au template
    result=phonenumber+' '+langue+' '+validite+' '+ txt +' '+user+ ' ID='+str(cle)
    return JsonResponse({'foo': 'bar'}) 

@login_required
def maj(request):
    #Vérifier permission
    #Récupération liste SMS des 24 dernières heures de l'unité
    Sms.objects
    liste=Sms.objects.filter(utilisateur='olivier')

    #Retour au template
    return HttpResponse(liste)

@login_required
def geoloc(request):
    Geoloc.objects
    liste=Geoloc.objects.all()
    return HttpResponse(liste) 


class SmsList(ListView):
    queryset = Sms.objects.all().order_by('-id')
    template_name = "gendloc/sms_list.html"
    context_object_name = 'sms_list'
    def get_queryset(self):
        ref =  datetime.now() - timedelta( hours = 240 )
        return self.queryset.filter(dt_envoi__gte=ref, unite='PG38')
        

class MapLayer(GeoJSONLayerView):
    # Options
    precision = 4   # float
    simplify = 0.5  # generalization


class SmsLoc(ListView):
    queryset = Sms.objects.select_related('loc').order_by('-id')
    template_name = "gendloc/smsloc_list.html"
    context_object_name = 'smsloc_list'
    def get_queryset(self):
        ref =  datetime.now() - timedelta( hours = 12 )
        return self.queryset.filter()
